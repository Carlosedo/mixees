from django.views.generic.base import TemplateView

class VueTemplateView(TemplateView):
    template_name = "core/index.html"
