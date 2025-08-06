from django.shortcuts import render
from .models import Notice

def notice_board(request):
    notices = Notice.objects.order_by('-date_posted')
    return render(request, 'notices/notice_board.html', {'notices': notices})