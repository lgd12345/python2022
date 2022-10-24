from email.quoprimime import body_check
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render

from myapp01.models import Board

# Create your views here.
# 업로드 될 폴더
UPLOAD_DIR = 'C:/Python/django/upload/'


# urls.py 설정해야함
# write_form
# 컨트롤러 역할
# 서버연결해야 들어가짐 write_form 함수이름
# 리턴은 board/write.html


def write_form(reqeust):
    return render(reqeust, 'board/write.html')


# csrf 쓰지 않겠다는 뜻임 위조방지하는 것
# insert
@csrf_exempt
def insert(reqeust):
    fname = ''
    fsize = 0

    if 'file' in reqeust.FILES:
        file = reqeust.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname),
                  'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    dto = Board(writer=reqeust.POST['writer'],
                title=reqeust.POST['title'],
                content=reqeust.POST['content'],
                filename=fname,
                filesize=fsize)
    dto.save()

    return redirect('/list/')

# 전체보기
# 딕형태로 만들어서처리{ : }


def list(reqeust):
    boardList = Board.objects.all()
    context = {'boardList': boardList}
    return render(reqeust, 'board/list.html', context)

# 상세보기
# {'dto':dto} context에 안 담고 딕을 바로 처리


def detail_idx(reqeust):
    id = reqeust.GET['idx']
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    return render(reqeust, 'board/detail.html', {'dto': dto})

# 레스트 방식 상세보기(detail/int:board_idx)


def detail(reqeust, board_idx):
    print('board_idx:', board_idx)
    id = board_idx
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()
    return render(reqeust, 'board/detail.html', {'dto': dto})


# 수정하기 폼


def update_form(reqeust, board_idx):
    print('board_idx 수정하기:', board_idx)
    dto = Board.objects.get(idx=board_idx)
    return render(reqeust, 'board/update.html', {'dto': dto})


# 수정하기

@csrf_exempt
def update(reqeust):
    # 파일 업로드 안 했으면 기존 값을 가져온다.
    id = reqeust.POST['idx']
    dto = Board.objects.get(idx=id)
    fname = dto.filename
    fsize = dto.filesize
    fhit = dto.hit
# 객체가 있으면 파일 객체를 받아온다.
# wb 읽기모드
    if 'file' in reqeust.FILES:
        file = reqeust.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname),
                  'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
# id, idx=reqeust.POST['idx'], 같은말
    update_dto = Board(id,
                       #    idx=reqeust.POST['idx'],
                       writer=reqeust.POST['writer'],
                       title=reqeust.POST['title'],
                       content=reqeust.POST['content'],
                       hit=fhit,
                       filename=fname,
                       filesize=fsize)
    update_dto.save()
    return redirect('/list')


# 삭제하기

# board_idx 인자값이 reqeust 2번으로 인식되고 있어서 reqeust를 직접적으로 안 쓰더라도 적어줘야 from자체인 reqeust에서 board_idx를 쓸 수 있다.
def delete(reqeust, board_idx):
    dto = Board.objects.get(idx=board_idx).delete()
    # dto.delete()
    return redirect('/list')
