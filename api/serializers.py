from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Video


class UserSerializer(serializers.ModelSerializer):
    # シリアライザーを装飾
    class Meta:
        # ベースとなるモデルを指定
        model = get_user_model()
        # 使用するフィールドを指定
        fields = ("email", "password", "username", "id")
        # フィールドの中から更に装飾が可能
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    # createメソッドをオーバーライド
    def create(self, validated_data):
        # models.pyで作成したcreate_userメソッドのハッシュ化されたパスワードをDBへ格納
        user = get_user_model().objects.create_user(**validated_data)

        return user


class VideoSerializer(serializers.ModelSerializer):
    # シリアライザーを装飾
    class Meta:
        # ベースとなるモデルを指定
        model = Video
        # 使用するフィールドを指定
        fields = ["id", "title", "video", "thum", "like", "dislike"]
