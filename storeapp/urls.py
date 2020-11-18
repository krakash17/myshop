from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from storeapp.views import CategoriesView,CategoryImageViewSet, CategoryView, ItemView, ItemsView, SubCategoriesView, SubCategoryView, UserView

urlpatterns = [
    path('user-list/', UserView.as_view(), name='user-list'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('subcategories/', SubCategoriesView.as_view(), name='subcategories'),
     path('items/', ItemsView.as_view(), name='item'),
    path('category/<pk>/', CategoryView.as_view(), name='category'),
    path('subcategory/<pk>/', SubCategoryView.as_view(), name='category'),
    path('item/<pk>/', ItemView.as_view(), name='category'),
    path('categoriespicture/<pk>/', CategoryImageViewSet.as_view(), name='profilepicture'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)