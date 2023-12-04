"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse

def api_guide(request):
    # API 엔드포인트에 대한 설명을 HTML 형식으로 작성하여 반환합니다.
    content = """
    <html>
    <head>
        <title>API 엔드포인트 안내</title>
    </head>
    <body>
        <h1>첫 로딩 페이지입니다.</h1>
        <p>아래 링크로 이동시 탭을 통해 모든 기능 사용 가능합니다.</p>
        <ul>
            <li><a href="/api/doctor_list">시작 페이지</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(content)

#from doctor import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('doctor/', views.index),
    path('api/', include('doctor.urls')),
    path('', api_guide),
]
