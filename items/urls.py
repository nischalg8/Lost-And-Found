from django.urls import path
from .views import list_items, detail_item, create_item, update_item, delete_item

app_name = "items"

urlpatterns = [
    path("", list_items, name="list_items"),
    path("create/", create_item, name="create_item"),
    path("<int:pk>/", detail_item, name="detail_item"),
    path("<int:pk>/update/", update_item, name="update_item"),
    path("<int:pk>/delete/", delete_item, name="delete_item"),
]