from django.urls import path
from pages.utils import ImageLocalStorage 
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, CartRemoveAllView, CartView, ImageViewFactory, ImageViewNoDI

urlpatterns = [ 
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/product_created', ProductCreateView.as_view(), name='product_created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'), 
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'), 
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'), 
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenodi_save'),    
] 