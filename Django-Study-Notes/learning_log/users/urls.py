"""为应用程序 users 定义 URL 模式。"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证 URL。
    path('', include('django.contrib.auth.urls')),
]
