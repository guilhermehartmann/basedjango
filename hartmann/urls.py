from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Linking modules
    #url(r'', include('social_auth.urls')),

    # Views in the base
    url(r"^$", views.HomepageView.as_view(), name="home"),

    # Adding new applications
    #url(r"^blog/", include("blog.urls", namespace="blog")),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

