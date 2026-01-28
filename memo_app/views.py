from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm

# 1. 박홍진 님 담당: 메모 생성 로직
def memo_create(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            # 민승민 님 담당: 로그인 기능 완성 전까지는 아래 두 줄은 선택사항입니다.
            if request.user.is_authenticated:
                memo.author = request.user
            memo.save()
            # 저장 후 동제 님이 만든 '목록 화면'으로 이동합니다.
            return redirect('memo_list') 
    else:
        form = MemoForm()
    
    # 박동제 님 담당: 템플릿 바인딩 (생성 화면)
    return render(request, 'memo_app/memo_form.html', {'form': form})

# 2. 유가영 님 담당: 메모 조회 로직 (중복 제거 및 통합)
def memo_list(request):
    # DB에서 모든 메모를 가져와 최신순으로 정렬합니다.
    memos = Memo.objects.all().order_by('-id')
    
    # 박동제 님 담당: 템플릿 바인딩 (목록 화면)
    # 가영 님이 만든 'memo_list.html'에 'memos' 데이터를 전달합니다.
    return render(request, 'memo_app/memo_list.html', {'memos': memos})

# 유가영 님 담당: 상세 조회 로직
def memo_detail(request, memo_id):
    # 해당 번호(memo_id)의 메모를 찾고, 없으면 404 에러를 띄웁니다.
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, 'memo_app/memo_detail.html', {'memo': memo})