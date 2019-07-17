from django.urls import path
from . import views
from .views import BookDetail, BookCreate, BookUpdate, BookDelete
app_name='books'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', BookCreate.as_view(), name='book_create'),
    path('<str:pk>/',  BookDetail.as_view(), name='book_detail'),
    path('<str:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('<str:pk>/delete/', BookDelete.as_view(), name='book_delete'),
]
