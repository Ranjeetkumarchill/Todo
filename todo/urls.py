from django.urls import path
from todo import views
urlpatterns = [
    path('', views.home, name='home'),
    path('del/<int:item_id>', views.remove, name='del'),
]
