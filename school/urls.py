from django.urls import path
from.import views

urlpatterns = [
		path('', views.index,name='index'),
		path('register/', views.register,name='register'),
		path('register_form/',views.register_form,name='register_form'),
		path('login/',views.login,name='login'),
		path('logout_don_bosco/',views.logout_don_bosco,name='logout_don_bosco'),
		
]