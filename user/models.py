from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator


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


class UserInfo(models.Model):

    class Meta:
        db_table = "userinfos"

    GENDER_CHOICES = (
        (0, "여성"),
        (1, "남성")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("작가 이름", max_length=16)
    gender = models.CharField("성별", max_length=4, choices=GENDER_CHOICES)
    birth = models.DateField("생일")
    email = models.EmailField("이메일", max_length=80, unique = True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone = models.CharField("연락처", validators = [phoneNumberRegex], max_length = 16, unique = True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    is_artist = models.BooleanField(default=False)


class ApplyLog(models.Model):

    class Meta:
        db_table = "approval_log"

    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    apply_date = models.DateTimeField(auto_now_add=True)
    examine_date = models.DateField(default=None, null=True)

    is_approval = models.BooleanField(default=None, null=True)
