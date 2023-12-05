from django.views import generic
from .models import *
from .forms import *

# ------------------------------------------------

# Index
class HomeView(generic.TemplateView):
    template_name = "index.html"

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
    success_url = HomeView()
    template_name = "comunidade_form.html"

class DeleteComunidade(generic.DeleteView):
    model = Comunidade
    success_url = HomeView()

class DetailComunidade(generic.DetailView):
    model = Comunidade
    template_name = "comunidade_detail.html"

# ------------------------------------------------

# Publicações

class CreatePublicacao(generic.CreateView):
    model = Publicacao
    form_class = PublicacaoForm
    success_url = HomeView()
    template_name = "publicacao_form.html"

class DeletePublicacao(generic.DeleteView):
    model = Publicacao
    success_url = HomeView()

class DetailPublicacao(generic.DetailView):
    model = Publicacao
    template_name = "publicacao_detail.html"

class UpdatePublicacao(generic.UpdateView):
    model = Publicacao
    form_class = PublicacaoForm
    template_name = "publicacao_form.html"

# class ReservaUpdateView(generic.UpdateView):
#   model = Reserva
#   form_class = ReservaForm
#   success_url = reverse_lazy("stands:reservas-list")
#   template_name = "reservas_form.html"