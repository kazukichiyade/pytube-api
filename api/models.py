from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# 複雑な文字列を作ってくれる
import uuid


# mediaの中のvideoディレクトリに保存(ファイル名も作成)
def load_path_video(instance, filename):
    return "/".join(["video", str(instance.title) + str(".mp4")])


# mediaの中のthumディレクトリに保存(ファイル名も作成)
def load_path_thum(instance, filename):
    # filenameから拡張子をextに格納
    ext = filename.split(".")[-1]
    return "/".join(["thum", str(instance.title) + str(".") + str(ext)])


# UserManagerモデル
# BaseUserManagerのuserNameからemailに変える為オーバーライドする
class UserManager(BaseUserManager):
    # user作成関数
    def create_user(self, email, password=None, **extra_fields):
        # emailが無ければエラーメッセージ
        if not email:
            raise ValueError("Email address is must")

        # normalize_email:大文字で入力された値を小文字に変換
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # superuser作成関数
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Userモデル
class User(AbstractBaseUser, PermissionsMixin):

    # uuidを使用した複雑な文字列をprimary keyにし編集不可に
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


# Videoモデル
class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=30, blank=False)
    # 動画ファイル
    video = models.FileField(blank=False, upload_to=load_path_video)
    # サムネイル画像
    thum = models.ImageField(blank=False, upload_to=load_path_thum)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.title