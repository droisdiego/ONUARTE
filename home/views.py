from django.views import generic

class HomeView(generic.TemplateView):
    template_name = "index.html"

# Create your views here.
