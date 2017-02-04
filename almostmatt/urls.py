from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'almostmatt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^eternal/', include('EternalDraft.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
