from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label): 
        return True
    
    @property
    def is_staff(self): 
        return self.is_admin


class Artist(models.Model):

    class Meta:
        db_table = "artist"

    GENDER_CHOICES = (
        ("F", "여성"),
        ("M", "남성")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField("작가 이름", max_length=16)
    gender = models.CharField("성별", max_length=4, choices=GENDER_CHOICES)
    birth = models.DateField("생일")
    email = models.EmailField("이메일", max_length=80, unique = True)
    phone = models.CharField("연락처", max_length = 18, unique = True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_artist = models.BooleanField(default=None, null=True)
