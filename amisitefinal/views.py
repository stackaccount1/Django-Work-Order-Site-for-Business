from django.views.generic import TemplateView

class HomePageView(TemplateView):

    template_name = 'wordorderapp/homepage.html'
