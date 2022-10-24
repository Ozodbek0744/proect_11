from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import registration_view, update_account_view, user_logout

app_name = 'account'


urlpatterns = [
    path('login', obtain_auth_token),
    path('register', registration_view),
    path('update', update_account_view),
    path('logout', user_logout)
]


