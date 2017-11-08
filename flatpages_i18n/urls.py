from django.conf.urls import url

from flatpages_i18n.views import redactor_upload
from flatpages_i18n.forms import FileForm, ImageForm

urlpatterns = (
    url('^upload/image/(?P<upload_to>.*)', redactor_upload, {
        'form_class': ImageForm,
        'response': lambda name, url: '<img src="%s" alt="%s" />' % (url, name),
        }, name='redactor_upload_image'),

    url('^upload/file/(?P<upload_to>.*)', redactor_upload, {
        'form_class': FileForm,
        'response': lambda name, url: '<a href="%s">%s</a>' % (url, name),
        }, name='redactor_upload_file'),
)
