from django.contrib import admin
from django.urls import path
from ladygit import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('contactdit/', views.contactdit, name='contactdit'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('deletecontact/<int:id>', views.deletecontact, name='deletecontact'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('success/', views.success, name='success'),
]
