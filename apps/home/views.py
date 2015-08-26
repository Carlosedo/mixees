from datetime import datetime

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        visits = self._get_visits()
        context['visits'] = visits

        return context

    def _get_visits(self):
        visits = self.request.session.get('visits', 1)
        last_visit = self.request.session.get('last_visit')
        reset_last_visit_time = False

        if last_visit:
            last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

            if (datetime.now() - last_visit_time).seconds > 5:
                visits += 1
                reset_last_visit_time = True
        else:
            reset_last_visit_time = True

        if reset_last_visit_time:
            self.request.session['last_visit'] = str(datetime.now())
            self.request.session['visits'] = visits

        return visits



class AboutView(TemplateView):
    template_name = "home/about.html"
