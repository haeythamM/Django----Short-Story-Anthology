from django.urls import path
from .views import CollectionList, CollectionDetail, CollectionCreate, CollectionUpdate, CollectionDelete, CoverCreate, StoryCreate

urlpatterns = [
    path("", CollectionList.as_view(), name="collections-home"),
    path("<int:pk>", CollectionDetail.as_view(), name="collection-detail"),
    path("add", CollectionCreate.as_view(), name="add-collection"),
    path("edit/<int:pk>", CollectionUpdate.as_view(), name="edit-collection"),
    path("delete/<int:pk>", CollectionDelete.as_view(), name="delete-collection"),
    path("cover/add/<int:pk>", CoverCreate.as_view(), name="add-cover"),
    path("story/add/<int:pk>", StoryCreate.as_view(), name="add-story"),
]