"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index,name='index'), #Root page
    path('admin_login',admin_login,name='admin_login'),
    path('letest_jobs',letest_jobs,name='letest_jobs'),
    
    


    # Recruiter 
    path('recruiter_signup',recruiter_signup,name='recruiter_signup'),
    path('recruiter_login',recruiter_login,name='recruiter_login'),
    path('recruiter_home',recruiter_home,name='recruiter_home'),
    path('add_job',add_job,name='add_job'),
    path('job_list',job_list,name='job_list'),
    path('job/<int:job_id>/delete/', delete_job, name='delete_job'),
    path('applied_candidatelist', applied_candidatelist, name='applied_candidatelist'),



    #User
    path('user_signup',user_signup,name='user_signup'),
    path('user_login',user_login,name='user_login'),
    path('user_home',user_home,name='user_home'),
    path('Logout',Logout,name='Logout'),
    path('user_letestjob',user_letestjob,name='user_letestjob'),
    path('job_detail/<int:pid>',job_detail,name='job_detail'),
    path('applyforjob/<int:pid>',applyforjob,name='applyforjob'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
