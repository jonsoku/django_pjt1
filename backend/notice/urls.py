from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.ListNotice.as_view()),
    path('<int:pk/>', views.DetailNotice.as_view())
]