from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('myproject.view',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    ('^hello/$','hello'),
    ('^time/$','current_time'),
    (r'time/plus/(\d{1,2})/$','hours_ahead'),
    (r'^contact/thanks/$','thanks'),
)

urlpatterns += patterns('myproject.books.views',(r'^search/$','search'))

urlpatterns += patterns('myproject.contact.views',
    (r'^contact/$','contact'),)
    
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),)
