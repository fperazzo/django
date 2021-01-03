from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views

from django.db.models import Sum, Avg, F
from django.db.models.functions import Coalesce


import json
import datetime

from proj_orc.models.models_pt1 import *

# from core.forms import Orc_pt1_Form


# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "core/index.html"

#Campos Gerados juntos com o Orçamento
# def gera_ops_orc(orcc):
#     orcopsonda = Orc_Operacao(idTipoOperacao_id=1, idorc=orcc)
#     orcopsonda.save()
#     sonda = OpSonda(diasdesonda=orcc.duracao, idorcop=orcopsonda)
#     sonda.save()


#View da criação de novo orçamento exemplo
# @login_required
# def pt1_new(request):
#      if request.method == "POST":
#          form = Orc_pt1_Form(request.POST)
#          if form.is_valid():
#              orc = form.save(commit=False)
#              orc.chave_proj = request.user
#              orc.save()
#              gera_ops_orc(orc)
#              return redirect('appequipagem:equipagem', idorc=orc.id)
#      else:
#          form = Orc_pt1_Form()
#      return render(request, 'core/neworc.html', {'form': form})

#View para listar os orçamentos do usuário
# @login_required
# def lista_orc_chave(request):
#     orcs = (
#         Orcamento.objects.filter(chave_proj=request.user)
#         .order_by('id')
#         )

#     for orc in orcs:
#         itens = Orc_Op_Item.objects.filter(idorcop__idorc_id=orc) #Filtrando os itens do orçamento orc
#         itscomvl = itens.values('idorcop__idorc') #Agrupando por orcamento idorc
#         itscomvl = itscomvl.aggregate(
#              #vtbrl = Sum(F('QTD') * F('iditem__vubrl')),
#              #vtusd = Sum(F('QTD') * F('iditem__vuusd')),
#              vtt_usd = Coalesce(Sum(F('QTD') * (F('iditem__vubrl') / orc.cambio + F('iditem__vuusd'))),0))

#         orc.comvlit = itscomvl #juntando no objeto orc o valor total dos itens

#     return render(request, 'core/lista_orc_chave.html', {'orcs': orcs})


# def cities_detail(request):

#     uf = request.GET["uf"]

#     cities_of_selected_uf = (
#         CityData.objects.filter(state=uf.upper())
#         .order_by("city")
#         .values_list("city", flat=True)
#     )

#     cities = list()
#     for city in cities_of_selected_uf:
#         cities.append({"name": city})
#     return HttpResponse(json.dumps(cities), content_type="application/json",)


# def cities_data(request):

#     queryset = Orcamento.objects.filter(chave_proj=request.user).order_by('id')
#     data = {
#         "uf": queryset.state,
#         "city": queryset.city,
#         "confirmed": queryset.confirmed,
#         "cases_rate_per_inhabitants": round(
#             ((queryset.confirmed / queryset.estimated_population_2019) * 100),
#             3,
#         ),
#         "deaths": queryset.deaths,
#         "deaths_rate_per_inhabitants": round(
#             ((queryset.deaths / queryset.estimated_population_2019) * 100), 3,
#         ),
#         "date": datetime.date.strftime(queryset.date, format="%d/%m/%Y"),
#         "estimated_population_2019": queryset.estimated_population_2019,
#     }

#     return HttpResponse(json.dumps(data), content_type="application/json")


#     def get_context_data(self, **kwargs):
#         cbio = self.object.cambio #cambio do orçamento
#         itens = Orc_Op_Item.objects.filter(idorcop__idorc_id=self.object) #Itens do orçamento
#         opscomvl = itens.values('idorcop__idTipoOperacao__nmtiposop') #Agrupando por tipo de operação
#         opscomvl = opscomvl.annotate(
#             vtbrl = Sum(F('QTD') * F('iditem__vubrl')),
#             vtusd = Sum(F('QTD') * F('iditem__vuusd')),
#             vtt_usd = Sum(F('QTD') * (F('iditem__vubrl') / cbio + F('iditem__vuusd'))),
#             )

#         context = super(ResumoOrcOpsView, self).get_context_data(**kwargs)
#         context['opscomvl'] = opscomvl
#         return context






  
# def add_zonas(request, pk):
#      codorc = Orcamento.objects.filter(chave_proj=request.user).order_by('-id')[0]    
#      queryset = Book.objects.filter(title__startswith='M')
#      codorc = get_object_or_404(queryset, pk=1)
#      post = get_object_or_404(Post, pk=pk)
#      if request.method == "POST":
#          form = PostForm(request.POST, instance=post)
#          if form.is_valid():
#              zona = form.save(commit=False)
#              post.author = request.user
#              post.published_date = timezone.now()
#              post.save()
#              return redirect('post_detail', pk=post.pk)
#      else:
#          form = PostForm(instance=post)
#      return render(request, 'blog/post_edit.html', {'form': form})

# class Pt1CreateView(LoginRequiredMixin,CreateView):
#     template_name = "core/pt1.html"
#     model = Orcamento
#     form_class = Orc_pt1_Form
#     success_url = reverse_lazy("core:index")

# def situacoes(request):
#     situacoes_met = (
#         Meto_situacao.objects.all()
#         .order_by("situacao")
#         .values_list("situacao", flat=True)
#         .distinct()
#     )

#     situacoes = list()
#     for situacao in situacoes_met:
#         situacoes.append({"situacao": situacao})

#     return render(
#         request,
#         "core/pt2.html",
#         {"situacoes": situacoes,},
#     )

# def sit_met(request):

#     situacao = request.GET['situacao']
#     metodo_of_selected_sit = (
#         Meto_situacao.objects.filter(situacao=situacao.upper())
#         .order_by("metodo")
#         .values_list("metodo", flat=True)
#     )
#     metodos = list()
#     for metodo in  metodo_of_selected_sit:
#         metodos.append({"name": metodo})
#     return HttpResponse(json.dumps(metodos), content_type="application/json",)

# def si_m(request):

#     si = request.GET['si']
#     if si == 'Produtor':
#         si = 'PROD'
#     elif si == 'Injetor':
#         si = 'INJ'
#     else:
#         si = 'PRODINJ'

#     metodo_of_selected_sit = (
#         Meto_situacao.objects.filter(situacao=si)
#         .order_by("metodo")
#         .values_list("metodo", flat=True)
#     )
#     metodos = list()
#     for metodo in  metodo_of_selected_sit:
#         metodos.append({"name": metodo})
#     return HttpResponse(json.dumps(metodos), content_type="application/json",)

# def mi_col(request):

#     si = request.GET['si']
#     mi = request.GET['mi']

#     col_of_selected_met = (
#         Colu_metodo.objects.filter(metodo=mi)
#         .order_by("coluna")
#         .values_list("coluna", flat=True)
#     )
#     colunas = list()
#     for coluna in  col_of_selected_met:
#         colunas.append({"name": coluna})
#     return HttpResponse(json.dumps(colunas), content_type="application/json",)


# results = PCT.objects.filter(code__startswith='a').values('id', 'name')
# return JsonResponse({'results': list(results)})
# returns {'results': [{'id': 1, 'name': 'foo'}, ...]}

# or if you only need the values:

# results = PCT.objects.filter(code__startswith='a').values_list('id', 'name')
# return JsonResponse({'results': list(results)})
# returns {'results': [[1, 'foo'], ...]}

#URLs.py
#https://tutorial.djangogirls.org/pt/django_forms/
#from django.urls import path 
# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
# ]



# from .forms import PostForm
# def post_new(request):
#      if request.method == "POST":
#          form = PostForm(request.POST)
#          if form.is_valid():
#              post = form.save(commit=False)
#              post.author = request.user
#              post.published_date = timezone.now()
#              post.save()
#              return redirect('post_detail', pk=post.pk)
#      else:
#          form = PostForm()
#      return render(request, 'blog/post_edit.html', {'form': form})

# 
# def post_edit(request, pk):
#      post = get_object_or_404(Post, pk=pk)
#      if request.method == "POST":
#          form = PostForm(request.POST, instance=post)
#          if form.is_valid():
#              post = form.save(commit=False)
#              post.author = request.user
#              post.published_date = timezone.now()
#              post.save()
#              return redirect('post_detail', pk=post.pk)
#      else:
#          form = PostForm(instance=post)
#      return render(request, 'blog/post_edit.html', {'form': form})




# if request.POST():
#     a_valid = formA.is_valid()
#     b_valid = formB.is_valid()
#     c_valid = formC.is_valid()
#     # we do this since 'and' short circuits and we want to check to whole page for form errors
#     if a_valid and b_valid and c_valid:
#         a = formA.save()
#         b = formB.save(commit=False)
#         c = formC.save(commit=False)
#         b.foreignkeytoA = a
#         b.save()
#         c.foreignkeytoB = b
#         c.save()