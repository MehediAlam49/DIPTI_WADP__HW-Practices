
from django.urls import path
from userAuth.views import *

urlpatterns = [
    # ----------Authenticate urls---------------
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    # ----------Pages urls---------------
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('teachers/', teachers, name='teachers'),
    path('registerTeacher/', registerTeacher, name='registerTeacher'),
]
