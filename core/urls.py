#from core.views import LocaisList, IndexTemplateView, LocalDetailView, RegCreateView, Pt1CreateView
from core.views import IndexTemplateView
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [


    path('', IndexTemplateView.as_view(), name="index"),
    path('pt1/', views.pt1_new, name='pt1'),



 ]
 
    # path('pt1/', Pt1CreateView.as_view(), name="pt1"),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('pt2/', situacoes, name="pt2"),  
    # path("sit_m/", sit_met, name="sit_m"),
    # path("si_m/", si_m, name="si_m"),
    # path("mi_col/", mi_col, name="mi_col"),
    # GET/POST /funcionario/{pk}
    #path('pt2/<pk>', Pt2UpdateView.as_view(), name="parte2"),
    # GET /localidades
    #path('locais/', LocaisList.as_view(), name="lista_locais"),
    # GET/POST /local_detail/{pk}
    #path('local_detail/<pk>', LocalDetailView.as_view(), name="detail_local"),
    # GET /aditivo/cadastrar
    #path('add_reg/', RegCreateView.as_view(), name="add_reg"),
    # GET/POST /pasta/{pk}
    #path('pasta/<pk>', PastaDetailView.as_view(), name="detail_pasta"),
    # GET /funcionarios
    # path('<int:pasta_id>/', views.getPastas, name='getPastas'),
    # GET /funcionarios
    #path('cpa/', PastaCreateView.as_view(), name="cpa"),
    # GET/POST /funcionario/{pk}
    #path('aditivo/<pk>', AditivoUpdateView.as_view(), name="atualiza_aditivo"),
    # GET/POST /funcionarios/excluir/{pk}
    #path('aditivo/excluir/<pk>', AditivoDeleteView.as_view(), name="deleta_aditivo"),