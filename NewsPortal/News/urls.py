from django.urls import path
from .views import PostsList, PostDetails, PostSearch, PostCreate, PostUpdate, PostDelete, subscriptions

urlpatterns =[
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetails.as_view(), name='post_detail'),
    path('search', PostSearch.as_view()),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions')
]