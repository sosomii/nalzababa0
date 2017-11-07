from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^place/$', views.index, name='list1'),
    url(r'^findlocal/$', views.findlocalindex, name='findlocals'),
    url(r'^dangjin/', views.dangjinindex, name='dangjinindex'),
    url(r'^incheon/', views.incheonindex, name='incheonindex'),
    url(r'^paju/', views.pajuindex, name='pajuindex'),
    url(r'^yangpyeong/', views.yangpyeongindex, name='yangpyeongindex'),
    url(r'^asan/', views.asanindex, name='asanindex'),
    url(r'^andong/', views.andongindex, name='andongindex'),
    #url(r'^place/$', include('traveler.urls')),
]
