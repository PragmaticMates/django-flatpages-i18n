from django.conf.urls import patterns

urlpatterns = patterns('flatpages_i18n.views', (r'^(?P<url>.*)$', 'flatpage'),)
