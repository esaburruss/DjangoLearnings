from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import hello, current_datetime, test
from home.views import *
from pages.views import *
from alumni.views import *
from mysite.functions import *
from image.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^imgUpload/$', handle_uploads),
    url(r'^loginHandler/$', loginHandler),
    url(r'^$', wrap(index, 'home')),
    url(r'^test/$', imgForm),
    url(r'^reOrder/$', reOrder),
    url(r'^page/(\d{1,2})/(\d{1,2})/$', wrap(page_load, 'diddle')),
    url(r'^pageEdit/(\d{1,2})/(\d{1,2})/$', wrapDash(pageEdit, 'diddle')),
    url(r'^pageEditAction/(\d{1,2})/(\d{1,2})/$', wrapDash(contentEdit, 'diddle')),
    url(r'^pageDelete/(\d{1,2})/(\d{1,2})/$', wrapDash(pageDelete, 'diddle')),
    url(r'^structure/$', wrapDash(structure, 'struct')),
    url(r'^dash/$', wrapDash(dashboard, 'dash')),
    url(r'^addAlumnus/$', wrap(addAlumnus, 'addAlum')),
    url(r'^addAlumnusAction/$', addAlumnusAction),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)