from django.urls import path

from . import views

urlpatterns = [
    path('create/laptop/', views.ProductViewSet.as_view({'post': 'create'})),
    path('list/laptop/', views.ProductViewSet.as_view({'get': 'list'})),
    path('detail/laptop/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('update/laptop/<int:pk>/', views.ProductViewSet.as_view({'put': 'update'})),
    path('destroy/laptop/<int:pk>/', views.ProductViewSet.as_view({'delete': 'destroy'})),
]
