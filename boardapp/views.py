import math
from django.shortcuts import render, get_object_or_404, redirect
from .models import DjangoBoard
from .forms import DjangoBoardForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, JsonResponse
import urllib, os, mimetypes
import json
from django.template.loader import render_to_string
# Create your views here.
def board(request):
    return render(request,'board.html')

def dataroom(request):
    #if request.method == 'GET' :
        
        # board_list = DataRoom.objects.all().order_by('-id')
        board_list = DjangoBoard.objects.all().order_by('-id')
        # 게시판 모든 글들을 대상으로 한다.
        num = 5
        paginator = Paginator(board_list, num)
        # 게시판 객체 num 개를 한 페이지로 자른다.
        board_page = request.GET.get('page')
        # request된 페이지를 변수에 담는다.
        post = paginator.get_page(board_page) 
        # request된 페이지를 얻어온 뒤 post에 저장
        page_numbers_range = 5
        #화면에 보여줄 페이지 번호 갯수
        max_index = len(paginator.page_range)
        current_page = int(board_page) if board_page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]    
        
        boards = DjangoBoard.objects.all().values('subject','professor').distinct()
        return render(request, 'dataroom.html', { 'post':post,'page_range':page_range,'board_list':boards}) 
    #elif request.method == 'POST':

      #  return render(request, 'dataroom.html')


def create(request):
    # 새로운 데이터 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        # 입력된 블로그 글들을 저장
        user = request.user
        form = DjangoBoardForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    post.filename = request.FILES['upload_files'].name
            post.save()
            form.save()
            return redirect('/dataroom/')
#         #글쓰기 페이지를 띄워주는 역할 == GET
        else:
            # 단순히 입력받을 수 있는 form을 띄우기
            form = DjangoBoardForm()
            return render(request, 'write.html',{'form':form})

# def update(request, board_id):
#     board_detail = get_object_or_404(DjangoBoard,pk=board_id)
#     if request.method == "POST":
#         # 수정할 게시판의 글 객체 가져오기
#         board_detail.sub = request.POST['edit_subject']
#         board_detail.item = request.POST['edit_item']
#         board_detail.year = timezone.datetime.now()
#         board_detail.title = request.POST['edit_title']
#         board_detail.save()
#         return redirect('dataroom')
#     else:
#         return render(request, 'edit.html',{'dataroom':board_detail} )
    #해당하는 게시판의 글 객체 pk에 맞는 입력공간

def delete(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    board_detail.delete()
    return redirect('dataroom')

def detail(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    return render(request, 'detail.html',{'dataroom':board_detail})

def write(request):
    form = DjangoBoardForm()
    return render(request,'write.html',{'form':form})

def edit(request, board_id):
    board_detail = get_object_or_404(DjangoBoard,pk=board_id)
    form = DjangoBoardForm(instance=board_detail)
    filename = board_detail.filename
    upload_files = board_detail.upload_files
    return render(request, 'edit.html',{'dataroom':board_detail, 'form': form, 'filename': filename, 'upload_files':upload_files} )

def file_download(request, pk):
    post = get_object_or_404(DjangoBoard, pk=pk)
    url = post.upload_files.url[1:]
    file_url = urllib.parse.unquote(url)
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(post.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
    return Http404

# def dataroom(request):
#     return render(request, 'data_room.html')
#     board_detail = get_object_or_404(DataRoom,pk=board_id)
#     return render(request, 'edit.html',{'dataroom':board_detail} )

def search(request):
    if request.method == 'POST':
        subject = json.loads(request.POST['search_value'])['subject']
        professor = json.loads(request.POST['search_value'])['professor']
    else:
        print("bye")
    data = dict()
    return render(request, 'dataroom.html',{'subject':subject,'professor':professor})
    