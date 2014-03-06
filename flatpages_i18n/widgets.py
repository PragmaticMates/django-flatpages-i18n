import json

from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.conf import settings


REDACTOR_OPTIONS = getattr(settings, 'FLATPAGES_REDACTOR_OPTIONS', {})

INIT_JS = """<script type="text/javascript">
  jQuery(document).ready(function(){
    $("#%s").redactor(%s);
  });
</script>
"""


class RedactorEditor(widgets.Textarea):
    class Media:
        js = (getattr(settings, 'FLATPAGES_REDACTOR_JS', 'js/redactor/redactor.js'), )
        css = {
            'all': (getattr(settings, 'FLATPAGES_REDACTOR_CSS', 'css/redactor/redactor.css'), )
        }

    def __init__(self, *args, **kwargs):
        super(RedactorEditor, self).__init__(*args, **kwargs)
        self.upload_to = kwargs.pop('upload_to', '')
        self.custom_options = kwargs.pop('redactor_options', {})

    def get_options(self):
        options = REDACTOR_OPTIONS.copy()
        options.update(self.custom_options)
        options.update({
            'imageUpload': reverse('redactor_upload_image', kwargs={'upload_to': self.upload_to}),
            'fileUpload': reverse('redactor_upload_file', kwargs={'upload_to': self.upload_to}),
            'minHeight': 400,
            'convertDivs': False,
        })
        return json.dumps(options)

    def render(self, name, value, attrs=None):
        html = super(RedactorEditor, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        html += INIT_JS % (id_, self.get_options())
        return mark_safe(html)


JQueryEditor = RedactorEditor