from django.urls import path
from .import views


urlpatterns = [
    path('author/', views.author, name='author'), 
    path('add',views.book_add,name='add'),
    path('list',views.list,name='book_list'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('details/<int:pk>/',views.book_details,name='book_details'),
    path('delete/<int:pk>/',views.book_delete, name='book_delete'),




 



]