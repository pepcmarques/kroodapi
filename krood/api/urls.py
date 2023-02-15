from django.urls import path

from krood.api import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('login/', views.LoginView.as_view(), name="example"),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
]