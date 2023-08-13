"""
URL configuration for Climatepulse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Climatepulse import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostView, PostDetailview,PostCreateView,PostUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='/'),
    path('aboutus/', views.aboutuspage, name="aboutus"),
    path('blogpage/', PostView.as_view(), name="blogpage"),
    path('post/<int:pk>', PostDetailview.as_view(), name="blog-post"),
    path('quizpage/', views.quizpage, name="quizpage"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logOutPage, name="logout"),
    path('addpost/',PostCreateView.as_view(), name="addpost"),
    path('post/edit/<int:pk>',PostUpdateView.as_view(), name="update_post"),

    path('saveenquiry/', views.saveEnquiry, name="saveenquiry"),
    path('profile/', views.profielPage, name="profile"),
    path('blogsearch/', views.blogSearch, name="blogsearch"),
    path('userblog/', views.userBlog, name="userblog"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
