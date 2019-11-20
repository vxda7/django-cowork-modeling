from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/reviews/new/', views.new, name="new"),
    path('<int:id>/reviews/<int:review_id>/delete/', views.delete, name="delete"),
    path('<int:id>/like/', views.like, name="like"),
]
