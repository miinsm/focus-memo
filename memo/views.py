from django.shortcuts import render, redirect
from .forms import MemoForm
from .models import Memo
from django.contrib import messages

def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            # 아직 로그인 기능이 없으므로 임시로 첫 번째 사용자 지정
            # (나중에 민승민님 로그인 구현 후 수정 예정)
            if request.user.is_authenticated:
                memo.author = request.user
            else:
                # 테스트용: 실제로는 로그인 필수로 바꿀 예정
                memo.author = None  # 또는 임시 사용자
            memo.save()
            messages.success(request, '메모가 저장되었습니다!')
            return redirect('memo_list')  # 나중에 목록 페이지로
        else:
            messages.error(request, '입력 내용을 확인해 주세요.')
    else:
        form = MemoForm()

    return render(request, 'memo/memo_form.html', {'form': form})