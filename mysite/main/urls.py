from django.urls import path
from . import views
from register import views as t

urlpatterns = [
    path("<int:id>", views.index, name = "index"),
    path("home/", views.home, name = "home"),
    path("create/", views.create, name = "create"),
    path("", views.default, name = "default"),
    path("logout/", t.logout, name = "logout"),
    path("view/", views.view, name = "view"),
    path('jurnal/', views.entry_list, name='entry_list'),
    path('add/', views.add_entry, name='add_entry'),
    path('informatii_dozare/', views.info_dozare,name='info_dozare'),
    path('resurse_medicale/',views.resurse_medicale,name="resurse_medicale"),
]

