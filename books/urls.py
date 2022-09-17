from .views import dashboard,book_details, book_delete, AddbookView, edit_view,update_book
from django.urls.conf import path, include


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("books/details/<int:pk>", book_details, name="book_details"),
    path("books/delete/<int:pk>", book_delete, name="book_delete"),
    path("books/add/", AddbookView.as_view(), name="add_book"),
    path("books/edit/<int:pk>", edit_view, name="edit_book"),
    path("books/edited/", update_book, name="update_book"),


]
