from django.urls import path

from . import views

urlpatterns = [
    path('create/product/', views.ProductViewSet.as_view({'post': 'create'})),
    path('list/products/', views.ProductViewSet.as_view({'get': 'list'})),
    path('detail/product/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('update/product/<int:pk>/', views.ProductViewSet.as_view({'put': 'update'})),
    path('destroy/product/<int:pk>/', views.ProductViewSet.as_view({'delete': 'destroy'})),
]
