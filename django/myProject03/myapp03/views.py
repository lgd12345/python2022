from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from myapp03.models import Board, Comment
from django.db.models import Q
import math
from django.http.response import JsonResponse, HttpResponse
import urllib.parse
from django.core.paginator import Paginator

# 같은 폴터의 forms라는 폴더에 UserForm 클래스를 쓰겠다.
from .forms import UserForm
# 회원가입 부분의 와 로그인
from django.contrib.auth import authenticate, login
# 멜론
from myapp03 import bigdataProcess


# 업로드될 폴더
UPLOAD_DIR = 'C:/Python/django/upload3/'

# Create your views here.

# base


def index(request):
    return render(request, "base.html")

# write


def write_form(request):
    return render(request, 'board/insert.html')

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
    return redirect('/list')

# list


# def list(request):
#     boardList = Board.objects.all()

#     # context = {'boardList':boardList}
#     return render(request, 'board/list.html', {'boardList': boardList})

#  # 검색 제외 한 페이징 전체 보기
# def list(request):
#     page = request.GET.get('page', 1)

#     # count
#     boardCount = Board.objects.all().count()
#     # 페이징 하기 123 [다음] [이전] 456 [다음] [이전] 7

#     pageSize = 5  # 한 화면의 게시글 수
#     blockPage = 3  # 보이는 페이지 수
#     currentPage = int(page)  # 현재 페이지

#     start = (currentPage-1)*pageSize
#     # 게시글의 전체 페이지 수 *(ceil올림) (게시글수 / pageSize)
#     totPage = math.ceil(boardCount / pageSize)
#     # (floor버림)
#     startPage = math.floor((currentPage-1)/blockPage)*blockPage + 1  # 7
#     endPage = startPage + blockPage - 1

#     if endPage > totPage:
#         endPage = totPage  # endPage

#     boardList = Board.objects.all().order_by("-id")[start:start+pageSize]

#     context = {'boardList': boardList,
#                'startPage': startPage,
#                'blockPage': blockPage,
#                'endPage': endPage,
#                'totPage': totPage,
#                'boardCount': boardCount,
#                'currentPage': currentPage,
#                'range': range(startPage, endPage+1)}
#     return render(request, 'board/list.html', context)

 # 검색 제외 한 페이징 전체 보기
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
    endPage = startPage + blockPage - 1

    if endPage > totPage:
        endPage = totPage  # endPage

    # 검색내용
    # Q 오알연산자
    # 검색을 하고 idx 에 대해서 내림차순으로 정렬
    if field == 'all':
        boardList = Board.objects.filter(Q(writer__contains=word) |
                                         Q(title__contains=word) |
                                         Q(content__contains=word)).order_by('-id')[start:start+pageSize]
    elif field == 'writer':
        boardList = Board.objects.filter(
            Q(writer__contains=word)).order_by('-id')[start:start+pageSize]
    elif field == 'title':
        boardList = Board.objects.filter(
            Q(title__contains=word)).order_by('-id')[start:start+pageSize]
    elif field == 'content':
        boardList = Board.objects.filter(
            Q(content__contains=word)).order_by('-id')[start:start+pageSize]
    else:
        boardList = Board.objects.all().order_by('-id')[start:start+pageSize]

    context = {'boardList': boardList,
               'startPage': startPage,
               'blockPage': blockPage,
               'endPage': endPage,
               'totPage': totPage,
               'boardCount': boardCount,
               'currentPage': currentPage,
               'range': range(startPage, endPage+1),
               'field': field,
               'word': word, }
    return render(request, 'board/list.html', context)

# 다운로드 횟수


def download_count(request):
    id = request.GET['id']
    dto = Board.objects.get(id=id)
    dto.down_up()
    dto.save()
    count = dto.down
    return JsonResponse({'id': id, 'count': count})


# 다운로드
def download(request):
    id = request.GET['id']
    dto = Board.objects.get(id=id)
    path = UPLOAD_DIR + dto.filename
    # 파일 네임을 잘 읽어 오게 하기(파일이름을 못 읽을 수 있어서)
    filename = urllib.parse.quote(dto.filename)
    # 파일을 스트림형태로 변환해서 다운로드 하기
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(),
                                content_type='application/octet-stream')
        response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(
            filename)
    return response
# list_page


# 장고가 가지고 있는 페이징 처리하는 (페이지 네이터)를 이용한 방식
# 셀렉터 빼고 인풋으로만 검색
def list_page(request):
    page = request.GET.get('page', '1')
    word = request.GET.get('word', '')

    boardCount = Board.objects.filter(Q(writer__contains=word) |
                                      Q(title__contains=word) |
                                      Q(content__contains=word)).count()
    boardList = Board.objects.filter(Q(writer__contains=word) |
                                     Q(title__contains=word) |
                                     Q(content__contains=word)).order_by('-id')

    pageSize = 5

    # 페이징 처리
    paginator = Paginator(boardList, pageSize)  # impord
    page_obj = paginator.get_page(page)
    print('boardCount', boardCount)

# 장고는 -가 없어서 (빼기)역할을 하는 함수를 따로 만들어준다ㅣ.
# 페이지 숫자 제대로 나오게                  #1페이지/2페이지/3페이지
    rowNo = boardCount - (int(page)-1) * pageSize  # 13 /13-5/13-10

    content = {'page_list': page_obj,
               'page': page,
               'word': word,
               'rowNo': rowNo,
               'boardCount': boardCount}
    return render(request, 'board/list_page.html', content)


# 상세보기 list_page


def detail_id(request):
    id = request.GET['id']
    dto = Board.objects.get(id=id)
    dto.hit_up()
    dto.save()

    return render(request, 'board/detail.html',
                  {'dto': dto})

# 레스트 방식 상세보기 (detail/<int:board_id>/)
# 관계성이 comment와 있기때문에 따로 적어주지 않아도 됨


def detail(request, board_id):
    id = board_id
    dto = Board.objects.get(id=id)
    dto.hit_up()
    dto.save()

    return render(request, 'board/detail.html', {'dto': dto})


# 수정하기 폼


def update_form(request, board_id):
    dto = Board.objects.get(id=board_id)
    return render(request, 'board/update.html', {'dto': dto})

# 수정하기


@csrf_exempt
def update(request):
    id = request.POST['id']
    dto = Board.objects.get(id=id)
    fname = dto.filename
    fsize = dto.filesize
    fhit = dto.hit
    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname),
                  'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
# id, id=request.POST['id'], 같은말
    update_dto = Board(id,
                       #    idx=request.POST['id'],
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
def delete(request, board_id):
    dto = Board.objects.get(id=board_id).delete()
    # dto.delete()
    return redirect('/list')

# 댓글


@csrf_exempt
def comment_insert(request):
    id = request.POST['id']
    dto = Comment(board_id=id,
                  writer="aa",
                  content=request.POST['content'])
    dto.save()
    return redirect('/detail/'+id)


# 회원가입
# 시큐리티가 다 되 어 있는 것을 사용할 것이다.
def signup(request):
    if request.method == "POST":     # 회원가입 insert부분임
        form = UserForm(request.POST)
        if form.is_valid():          # 유효성
            print('signup POST valid')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('/')

        else:
            print('signup POST un_valid')

    else:                # 회원가입 폼으로 가라
        form = UserForm()

    return render(request, 'common/signup.html', {'form': form})


#################################################
# 멜론


def melon(request):
    bigdataProcess.melon_crawing()
    return render(request, "bigdata/melon.html")
