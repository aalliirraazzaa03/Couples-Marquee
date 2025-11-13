# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DecorViewSet, EventsWithoutDecorAmount, decor_summary
# from .views import DecorImageUploadView, DecorImageListView


# router = DefaultRouter()
# router.register(r'', DecorViewSet, basename='decor')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('events/without-decor/', EventsWithoutDecorAmount.as_view(), name='events-without-decor'),
#     path('summary/', decor_summary, name='decor-summary'),
#     path('images/upload/', DecorImageUploadView.as_view(), name='upload-images'),
#     path('images/', DecorImageListView.as_view(), name='list-images'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DecorViewSet, EventsWithoutDecorAmount, decor_summary
from .views import DecorImageUploadView, DecorImageListView,CreateImageFolderView,DecorFoldersWithImagesView

router = DefaultRouter()
router.register(r'', DecorViewSet, basename='decor')

urlpatterns = [

    
    # Image endpoints FIRST
    path('images/upload/', DecorImageUploadView.as_view(), name='upload-images'),
    path('images/', DecorImageListView.as_view(), name='list-images'),
    path('images/create-folder/', CreateImageFolderView.as_view(), name='create-image-folder'),
    path('images/folders/', DecorFoldersWithImagesView.as_view(), name='list-folders-with-images'),

    # Then other endpoints
    path('events/without-decor/', EventsWithoutDecorAmount.as_view(), name='events-without-decor'),
    path('summary/', decor_summary, name='decor-summary'),

    # Router last (so it doesn’t override others)
    path('', include(router.urls)),
]
