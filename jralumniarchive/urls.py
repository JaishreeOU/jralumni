

from django.urls import path
from . import views

app_name = "jralumniarchive"

urlpatterns = [
    path('justsomepage/', views.justsomepage, name='justsomepage'),
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('families/', views.FamilyListView.as_view(), name='families'),
    path('x', views.student_list, name='student_list'),
#    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
