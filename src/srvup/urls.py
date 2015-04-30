from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers


from comments.serializers import CommentViewSet
from comments.views import CommentCreateAPIView, CommentDetailAPIView, CommentListAPIView
from videos.serializers import CategoryViewSet, VideoViewSet
from videos.views import CategoryListAPIView, CategoryDetailAPIView, VideoDetailAPIView

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"videos", VideoViewSet)


urlpatterns = patterns('',
    url(r'^jquery-test/$', 'srvup.views.jquery_test_view'),
    url(r'^api2/$', 'srvup.views.api_home_abc', name='api_home'),
    url(r'^api2/comment/$',
        CommentListAPIView.as_view(),
        name='comment_list_api',
        ),
    url(r'^api2/comment/create/$',
        CommentCreateAPIView.as_view(),
        name='comment_create_api',
        ),
    url(r'^api2/comment/(?P<id>\d+)/$',
        CommentDetailAPIView.as_view(),
        name='comment_detail_api',
        ),
    url(r'^api2/projects/$', 
            CategoryListAPIView.as_view(), 
            name='category_list_api'),
    url(r'^api2/projects/(?P<slug>[\w-]+)/$', 
                CategoryDetailAPIView.as_view(),
                 name='category_detail_api'),
    url(r'^api2/projects/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', 
            VideoDetailAPIView.as_view(), 
            name='video_detail_api'),


    # Examples:
    #url(r'^about/$', TemplateView.as_view(template_name='base.html'), name='home'),
    #url(r'^pricing/$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^contact/$', TemplateView.as_view(template_name='company/contact_us.html'), name='contact_us'),
    url(r'^$', 'srvup.views.home', name='home'),
    url(r'^projects/$', 'videos.views.category_list', name='projects'),
    url(r'^projects/(?P<cat_slug>[\w-]+)/$', 'videos.views.category_detail', name='project_detail'),
    url(r'^projects/(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', 'videos.views.video_detail', name='video_detail'),
    url(r'^dj/admin/', include(admin.site.urls)),
    url(r'^api/auth/token/$', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
) 

if settings.DEBUG:
    urlpatterns += patterns('',) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += patterns('',) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#auth login/logout
urlpatterns += patterns('billing.views',
    url(r'^upgrade/$', 'upgrade', name='account_upgrade'),
    url(r'^billing/$', 'billing_history', name='billing_history'),
    url(r'^billing/cancel/$', 'cancel_subscription', name='cancel_subscription'),
)



#auth login/logout
urlpatterns += patterns('accounts.views',
    url(r'^account/$', 'account_home', name='account_home'),
	url(r'^logout/$', 'auth_logout', name='logout'),
    url(r'^login/$', 'auth_login', name='login'),
    url(r'^register/$', 'auth_register', name='register'),
)



#Comment Thread
urlpatterns += patterns('comments.views',
    url(r'^comment/(?P<id>\d+)$', 'comment_thread', name='comment_thread'),
    url(r'^comment/create/$', 'comment_create_view', name='comment_create'),
)


#Notifications
urlpatterns += patterns('notifications.views',
    url(r'^notifications/$', 'all', name='notifications_all'),
    url(r'^notifications/ajax/$', 'get_notifications_ajax', name='get_notifications_ajax'),
    url(r'^notifications/(?P<id>\d+)/$', 'read', name='notifications_read'),

)



