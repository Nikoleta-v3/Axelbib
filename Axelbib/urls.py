from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet, 'article')
router.register(r'author', views.AuthorViewSet, 'author-list')
router.register(r'year', views.YearViewSet, 'year-list')
router.register(r'label', views.LabelViewSet, 'label-list')
router.register(r'strategies', views.StrategiesViewSet, 'strategies-list')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls, namespace='models')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
