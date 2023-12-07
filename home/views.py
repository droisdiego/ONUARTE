from django.views import generic
from .models import *
from .forms import ComunidadeForm, PublicacaoForm
# from django.contrib.auth.decorators import login_required

# ------------------------------------------------

# Account-Allauth

# class CustomSignupView(SignupView):
#     template_name = 'register.html'
#     form_class = CustomSignupForm

# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     form_class = CustomLoginForm




# ------------------------------------------------


# Index
class ListaPublicacoes(generic.ListView):
    model = Publicacao
    template_name = "index.html"
    context_object_name = "publicacoes"
    def get_queryset(self):
        return Publicacao.objects.order_by('-data_publicacao')
# class HomeView(generic.TemplateView):
#     template_name = "index.html"

# ------------------------------------------------

# Usuario
class DetailUsuario(generic.DetailView):
    model = PerfilUsuario
    template_name = "usuario_detail.html"


# ------------------------------------------------

# Comunidade
class CreateComunidade(generic.CreateView):
    model = Comunidade
    form_class = ComunidadeForm
    success_url = ListaPublicacoes()
    template_name = "comunidade_form.html"

class DeleteComunidade(generic.DeleteView):
    model = Comunidade
    success_url = ListaPublicacoes()

class DetailComunidade(generic.DetailView):
    model = Comunidade
    template_name = "comunidade_detail.html"

# ------------------------------------------------

# Publicações

class CreatePublicacao(generic.CreateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = ListaPublicacoes()
    template_name = "publicacao_form.html"

class DeletePublicacao(generic.DeleteView):
    model = Publicacao
    success_url = ListaPublicacoes()

class DetailPublicacao(generic.DetailView):
    model = Publicacao
    template_name = "publicacao_detail.html"

class UpdatePublicacao(generic.UpdateView):
    model = Publicacao
    form_class = PublicacaoForm
    template_name = "publicacao_form.html"
