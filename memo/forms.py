from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']  # 지금은 category 없으니까 content만!
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 8,
                'placeholder': '자유롭게 메모를 작성하세요...',
                'class': 'form-control',
            }),
        }