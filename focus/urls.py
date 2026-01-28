from django.contrib import admin
from django.urls import path, include
from memo import views as memo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('memo/', include('memo.urls')),

    path("accounts/register/", memo_views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]