from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import VideoViewSet, CreateUserView

router = routers.DefaultRouter()
# ModelViewSetを使用した場合はrouter.registerを使用する
router.register("videos", VideoViewSet)

urlpatterns = [
    # CreateUserViewはCreateAPIViewという汎用Viewを使っているのでas_view()のてurlpatternsに記載
    path("create/", CreateUserView.as_view(), name="create"),
    path("", include(router.urls)),
]