
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render

from django.http.response import JsonResponse, HttpResponse
import urllib.parse
from django.db.models import Q
import math

from myapp01.models import Board, Comment


# Create your views here.
# 업로드 될 폴더
UPLOAD_DIR = 'C:/Python/django/upload/'


# urls.py 설정해야함
# write_form
# 컨트롤러 역할
# 서버연결해야 들어가짐 write_form 함수이름
# 리턴은 board/write.html


def write_form(request):
    return render(request, 'board/write.html')


# csrf 쓰지 않겠다는 뜻임 위조방지하는 것
# insert
@csrf_exempt
def insert(request):
    fname = ''
    fsize = 0

    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname),
                  'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    dto = Board(writer=request.POST['writer'],
                title=request.POST['title'],
                content=request.POST['content'],
                filename=fname,
                filesize=fsize)
    dto.save()

    return redirect('/list/')

# 전체보기
# 딕형태로 만들어서처리{ : }


# def list(request):
#     boardList = Board.objects.all()
#     context = {'boardList': boardList}
#     return render(request, 'board/list.html', context)

    # 전체 보기 검색기능
def list(request):
    page = request.GET.get('page', 1)
    word = request.GET.get('word', '')
    field = request.GET.get('field', 'title')

    # count
    if field == 'all':
        boardCount = Board.objects.filter(Q(writer__contains=word) |
                                          Q(title__contains=word) |
                                          Q(content__contains=word)).count()
    elif field == 'writer':
        boardCount = Board.objects.filter(
            Q(writer__contains=word)).count()
    elif field == 'title':
        boardCount = Board.objects.filter(
            Q(title__contains=word)).count()
    elif field == 'content':
        boardCount = Board.objects.filter(
            Q(content__contains=word)).count()
    else:
        boardCount = Board.objects.all().count()

    # 페이징 하기 123 [다음] [이전] 456 [다음] [이전] 7

    pageSize = 5  # 한 화면의 게시글 수
    blockPage = 3  # 보이는 페이지 수
    currentPage = int(page)  # 현재 페이지

    start = (currentPage-1)*pageSize
    # 게시글의 전체 페이지 수 *(ceil올림) (게시글수 / pageSize)
    totPage = math.ceil(boardCount / pageSize)
    # (floor버림)
    startPage = math.floor((currentPage-1)/blockPage)*blockPage + 1  # 7
    endPage = startPage + blockPage - 1  # 9

    if endPage > totPage:
        endPage = totPage  # endPage = 7

    # 검색내용
    # Q 오알연산자
    # 검색을 하고 idx 에 대해서 내림차순으로 정렬
    if field == 'all':
        boardList = Board.objects.filter(Q(writer__contains=word) |
                                         Q(title__contains=word) |
                                         Q(content__contains=word)).order_by('-idx')[start:start+pageSize]
    elif field == 'writer':
        boardList = Board.objects.filter(
            Q(writer__contains=word)).order_by('-idx')[start:start+pageSize]
    elif field == 'title':
        boardList = Board.objects.filter(
            Q(title__contains=word)).order_by('-idx')[start:start+pageSize]
    elif field == 'content':
        boardList = Board.objects.filter(
            Q(content__contains=word)).order_by('-idx')[start:start+pageSize]
    else:
        boardList = Board.objects.all().order_by('-idx')[start:start+pageSize]

    context = {'boardList': boardList,
               'startPage': startPage,
               'blockPage': blockPage,
               'endPage': endPage,
               'totPage': totPage,
               'boardCount': boardCount,
               'currentPage': currentPage,
               'field': field,
               'word': word,
               'range': range(startPage, endPage+1)}
    return render(request, 'board/list.html', context)


# 상세보기
# {'dto':dto} context에 안 담고 딕을 바로 처리


def detail_idx(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()

    # comment 댓글 list
    commentList = Comment.objects.filter(board_idx=id).order_by
    ('-idx')

    return render(request, 'board/detail.html',
                  {'dto': dto,
                   'commentList': commentList})

# 레스트 방식 상세보기(detail/int:board_idx)


def detail(request, board_idx):
    print('board_idx:', board_idx)
    id = board_idx
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()

    # comment 댓글 list
    # 관계성이 없다고 판단해서 이런식으로 표현했다.
    commentList = Comment.objects.filter(board_idx=id).order_by
    ('-idx')

    return render(request, 'board/detail.html', {'dto': dto,
                                                 'commentList': commentList})


# 수정하기 폼


def update_form(request, board_idx):
    print('board_idx 수정하기:', board_idx)
    dto = Board.objects.get(idx=board_idx)
    return render(request, 'board/update.html', {'dto': dto})


# 수정하기

@csrf_exempt
def update(request):
    # 파일 업로드 안 했으면 기존 값을 가져온다.
    id = request.POST['idx']
    dto = Board.objects.get(idx=id)
    fname = dto.filename
    fsize = dto.filesize
    fhit = dto.hit
# 객체가 있으면 파일 객체를 받아온다.
# wb 읽기모드
    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname),
                  'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
# id, idx=request.POST['idx'], 같은말
    update_dto = Board(id,
                       #    idx=request.POST['idx'],
                       writer=request.POST['writer'],
                       title=request.POST['title'],
                       content=request.POST['content'],
                       hit=fhit,
                       filename=fname,
                       filesize=fsize)
    update_dto.save()
    return redirect('/list')


# 삭제하기

# board_idx 인자값이 request 2번으로 인식되고 있어서 request를 직접적으로 안 쓰더라도 적어줘야 from자체인 request에서 board_idx를 쓸 수 있다.
def delete(request, board_idx):
    dto = Board.objects.get(idx=board_idx).delete()
    # dto.delete()
    return redirect('/list')

# 다운로드 횟수


def download_count(request):
    id = request.GET['idx']
    print('id: ', id)

    dto = Board.objects.get(idx=id)
    dto.down_up()
    dto.save()
    count = dto.down
    print('count : ', count)
    return JsonResponse({'idx': id, 'count': count})

# 다운로드
# with open(path,'rb') as file: 읽기모드


def download(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    path = UPLOAD_DIR + dto.filename
    filename = urllib.parse.quote(dto.filename)
    print('filename:', filename)
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(),
                                content_type='application/octet-stream')
        response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(
            filename)
    return response

# comment 댓글
# post방식 csrf 안 쓰겠다.


@csrf_exempt
def comment_insert(request):
    id = request.POST['idx']
    dto = Comment(board_idx=id,
                  writer='aa',
                  content=request.POST['content'])
    dto.save()
    return redirect("/detail_idx?idx="+id)
