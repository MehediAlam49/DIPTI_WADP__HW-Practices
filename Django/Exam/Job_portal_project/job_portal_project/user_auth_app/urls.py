from django.urls import path
from user_auth_app.views import *

urlpatterns = [
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('home/', home, name='home'),
    path('pendingAccountList/', pendingAccountList, name='pendingAccountList'),
    path('acceptPendingAccount/<str:id>', acceptPendingAccount, name='acceptPendingAccount'),
    
]