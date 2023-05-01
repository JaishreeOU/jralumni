

from django.urls import path
from . import views
# app_name = "jralumniarchive"

urlpatterns = [
    path('justsomepage/', views.justsomepage, name='justsomepage'),
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('familiesf/', views.family_list, name='familiesf'),
    path('familiesgc/', views.FamilyListView.as_view(), name='familiesgc'),

    path('familygc/<int:pk>', views.FamilyDetailView.as_view(), name='alumnifamily-detailgc'),


    path('studentsf/', views.student_list, name='studentsf'),
    path('studentsgc/', views.StudentListView.as_view(), name='studentsgc'),

    path('x', views.student_list, name='student_list'),
#    path("families/<int:pk>/", views.DetailView.as_view(), name="detail"),


]


