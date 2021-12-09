from django.urls import path

from . import views

urlpatterns = [
    path('create/product/', views.ProductCreateView.as_view()),
    path('list/products/', views.ProductListViewSet.as_view({'get': 'list'})),
    path('detail/product/<int:pk>/', views.ProductDetailView.as_view()),
    path('update/product/<int:pk>/', views.ProductUpdateView.as_view()),
    path('destroy/product/<int:pk>/', views.ProductDeleteView.as_view()),
]
