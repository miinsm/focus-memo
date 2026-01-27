from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MemoForm
from .models import Memo
from django.contrib import messages

@login_required  # 로그인한 사용자만 접근 가능
@login_required
def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.author = request.user
            memo.save()
            messages.success(request, '메모가 저장되었습니다!')
            return redirect('memo_list')  # ✅ 수정 포인트
    else:
        form = MemoForm()

    return render(request, 'memo/memo_form.html', {'form': form})
