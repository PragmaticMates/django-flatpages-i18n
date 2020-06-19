from django.views.generic import DetailView as DjangoDetailView

from flatpages_i18n.models import FlatPage_i18n


class DetailView(DjangoDetailView):
    model = FlatPage_i18n
    template_name = 'flatpages_i18n/default.html'
    slug_field = 'slug_i18n'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        # TODO: check registration_required
        # TODO: check template_name
        return super().dispatch(request, *args, **kwargs)
