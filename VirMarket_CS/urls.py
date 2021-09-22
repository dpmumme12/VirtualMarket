from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ArticleViewset, basename='article')

urlpatterns = [
    #path('v1', views.article_list, name='api'),
    # path('v1', views.articleAPIView.as_view()),
    # path('v1/<int:id>', views.article_details.as_view()),
    path('generic/<int:id>/', views.genericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls))
]