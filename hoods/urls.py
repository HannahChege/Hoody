from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.hood,name = 'hood'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^new/hood$', views.new_hood, name='new-hood'),
    url(r'^create/post$', views.create_post, name='create-post'),
    url(r'join/$', views.join, name='join'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^newprofile/', views.new_profile, name='new_profile'),
    url(r'^business/', views.business, name='business'),
    url(r'^newbusiness/', views.new_business, name='new_business'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)