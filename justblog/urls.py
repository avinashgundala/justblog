from django.contrib import admin
from django.urls import path,include,re_path
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('blog/api/',include('blog.api.urls')),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    re_path(r'^profile/(?P<username>\w+)/$',user_views.profile_detail,name='profile-detail'),
    path('login/',auth_views.LoginView.as_view(template_name ='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
