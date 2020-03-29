from django.urls import path
from django.views.decorators.http import require_POST, require_GET

from accounts.views import AddAccounts

urlpatterns = [
    path('account/user/register/',
         require_GET(AddAccounts.as_view())
         ),  # 用户注册
]
