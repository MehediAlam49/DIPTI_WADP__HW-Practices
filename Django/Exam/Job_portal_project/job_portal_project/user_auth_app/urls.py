from django.urls import path
from user_auth_app.views import *

urlpatterns = [
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('pendingAccountList/', pendingAccountList, name='pendingAccountList'),
    path('acceptPendingAccount/<str:id>', acceptPendingAccount, name='acceptPendingAccount'),
    path('rejectPendingAccount/<str:id>', rejectPendingAccount, name='rejectPendingAccount'),
    path('changePassword/', changePassword, name='changePassword'),
    
]