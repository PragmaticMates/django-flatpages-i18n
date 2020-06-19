from django.urls import path

from flatpages_i18n.views import DetailView

app_name = 'flatpages_i18n'

urlpatterns = [
    path('<str:slug>/', DetailView.as_view(), name='detail')
]
