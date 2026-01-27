from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import MemoForm
from .models import Memo

# (임시) 로그인 붙일 땐 주석 해제
# from django.contrib.auth.decorators import login_required


# @login_required
def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)

            # 로그인 붙일 때만 사용
            # memo.author = request.user

            memo.save()
            messages.success(request, '메모가 저장되었습니다!')
            return redirect('memo_list')
        else:
            messages.error(request, '입력 내용을 확인해 주세요.')
    else:
        form = MemoForm()

    return render(request, 'memo/memo_form.html', {'form': form})


# @login_required
def memo_list(request):
    """
    메모 목록
    - 최신순 기본(모델 Meta ordering 있어도 OK)
    - (임시) 전체 조회
    - (로그인 붙이면) author=request.user로 필터
    """
    q = request.GET.get('q', '').strip()

    qs = Memo.objects.all()

    # 로그인 붙일 때만 활성화
    # qs = qs.filter(author=request.user)

    if q:
        qs = qs.filter(content__icontains=q)

    memos = qs.order_by('-created_at')

    return render(request, 'memo/memo_list.html', {
        'memos': memos,
        'q': q,
    })


# @login_required
def memo_detail(request, memo_id):
    """
    메모 상세
    - (임시) 전체에서 id로 조회
    - (로그인 붙이면) author=request.user 조건 추가
    """
    memo = get_object_or_404(Memo, id=memo_id)

    # 로그인 붙일 때만
    # memo = get_object_or_404(Memo, id=memo_id, author=request.user)

    return render(request, 'memo/memo_detail.html', {'memo': memo})
