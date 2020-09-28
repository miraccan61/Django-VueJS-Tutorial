"""from .views import index
from django.urls import path


from rest_framework import routers
from api.views import ArticleViewSet

router = routers.DefaultRouter()
router.register('article', ArticleViewSet)

urlpatterns = [
    path('', index, name="home")

]
"""