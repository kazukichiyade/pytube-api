from rest_framework import viewsets
from rest_framework import generics
from .serializers import VideoSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from .models import Video


# Userを新規作成するView
class CreateUserView(generics.CreateAPIView):
    # 使用するシリアライザー指定
    serializer_class = UserSerializer

    # 開発時なのであらゆるユーザーがアクセスできるように設定
    permission_classes = (AllowAny,)


# 動画の一覧を取得、新規作成、削除するView
class VideoViewSet(viewsets.ModelViewSet):
    # modelのオブジェクトを全取得
    queryset = Video.objects.all()

    # 使用するシリアライザー指定
    serializer_class = VideoSerializer