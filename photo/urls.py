from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('photos/<int:category>', views.CategoryView.as_view(), name='photos_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('photo-detail/<int:pk>', views.DetailsView.as_view(), name='photo_detail'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('photo/<int:pk>/delete', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('materials/<int:class_id>/', views.MaterialListView.as_view(), name='material_list'),
    path('material/<int:pk>/', views.MaterialDetailView.as_view(), name='material_detail'),
    path('materials/create/', views.MaterialCreateView.as_view(), name='material_create'),
]