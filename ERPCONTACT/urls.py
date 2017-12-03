from django.conf.urls import url
import contact.views as ct_views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls, name = 'admin'),
    url(r'$^', ct_views.contact, name = 'index'),
    url(r'^contact$', ct_views.contact, name = 'contact'),
    url(r'^contact/success', ct_views.contact_success, name='contact_success'),
    url(r'^work$', ct_views.work, name='work'),
    url(r'^work/findbycompany/', ct_views.work_find_by_company, name='work_find_by_company'),
    url(r'^work/findbyitemid/', ct_views.work_find_by_itemid, name='work_find_by_itemid'),
    url(r'^comment$'), ct_views.post_comment, name='post_comment')
]