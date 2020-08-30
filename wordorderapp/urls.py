from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'wordorderapp'

urlpatterns = [
    path('', views.HomePage1View.as_view(), name='home1'),
    path('workorder/', views.IndexView.as_view(), name='index'),
    path('workorder/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('workorderinvoicesent/', views.IndexView1.as_view(), name='index1'),
    path('workordertotallist/', views.IndexView2.as_view(), name='index2'),
    path('workordercreate/', views.WorkCreate.as_view(), name='creatework'),
    path('workorderupdate/<int:pk>/', views.WorkUpdate.as_view(), name='updatework'),
    path('workorderupdate1/<int:pk>/', views.WorkUpdate1.as_view(), name='updatework1'),
    path('workorderupdateadmin/<int:pk>/', views.WorkUpdateAdmin.as_view, name='updateworkadmin'),
    path('workorderdelete/', views.WorkDelete.as_view(), name='workorderdelete'),
    path('dailyjournal/', views.DailyCreate.as_view(), name='daily'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('search/', views.WorkOrderSearchView.as_view(), name='search'),
    path('logoutsuccess/', views.LogoutSuccessView.as_view(), name='logoutsuccess'),
    path('loginsuccess/', views.LoginSuccessView.as_view(), name='loginsuccess')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
