"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from play import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.func ,name='func'),
    path('upload/',views.func1 ,name='upload'),
    path('update/<int:u_id>',views.func2,name='update'),
    path('delete/<int:d_id>' ,views.func3 ,name='delete'),
    path('upload1/',views.func4 ,name='upload1'),
    path('update1/<str:u_id>',views.func5),
    path('delete1/<str:d_id>' ,views.func6),
    path('upload2/',views.func7 ,name='upload2'),
    path('update2/<str:u_id>',views.func8),
    path('delete2/<str:d_id>' ,views.func9),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
]
