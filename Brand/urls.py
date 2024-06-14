from django.urls import path
from .import views

urlpatterns = [
    path('',views.UserLoginView.as_view(),name='login'),
    path('Signup/',views.userRegistrationView.as_view(),name='signUp'),
    path('Log',views.User_Logout,name='logout'),
    path('Brand',views.BrandRegistrationView.as_view(),name='Reg'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail'),
    path('buy/<int:id>/', views.buy_car, name='buy'),
    path('Profile_edit/', views.edit_profile, name='Profile_edit'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
]
