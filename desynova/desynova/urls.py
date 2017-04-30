from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.landing_page),
    url(r'^short_url/$', views.short_url),
    url(r'^short_url/(?P<short_url_id>[\w\-]+)/$', views.redirect_url),
    url(r'^paste_lockly/$', views.paste_lockly),
    url(r'^paste_lockly/(?P<share_url_id>[\w\-]+)/$', views.decode_content),
    url(r'^decode_content/$', views.get_decode_content),
    url(r'^get_neft_data/$', views.get_neft_data),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
