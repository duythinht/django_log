from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^logs/(\d*)$', 'home.views.logs', name='logs'),
    url(r'^delete/(\d*)$', 'home.views.delete', name='delete'),
    # url(r'^logs/', include('logs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
