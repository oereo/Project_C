#from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, nickname ,date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            nickname = nickname,
            phone_number = phone_number,
            #phoneNumber = phoneNumber,
        )
        #user.is_seller = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_bussiness_user(self, email, business_number, team, phone_number, nickname ,date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            nickname = nickname,
            phone_number = phone_number,
            team = team,
            business_number = business_number,
            #seller_name = seller_name,
            # is_seller = is_seller,
            #phoneNumber = phoneNumber,
        )
        #user.is_seller = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, nickname, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            nickname = nickname,
            phone_number = phone_number,
            
            #phoneNumber = phoneNumber,

        )
        #user.is_seller = False
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )

    MODE_CHOICES = (
    ('서울', '서울'), 
    ('부산', '부산'),
    ('대전', '대전'),
    ('대구', '대구'),
    ('인천', '인천'),
    ('강릉', '강릉'),
    )
    phone_number = models.CharField(max_length=14, null = False, unique = True)
    date_of_birth = models.DateField()
    business_number = models.CharField(max_length = 30, null = True, unique = True, choices = MODE_CHOICES) 
    team = models.CharField(max_length = 10, null = True, unique = True)
    #seller_name = models.CharField(max_length = 30, null = True, unique = True)

    #phoneNumber = PhoneNumberField(_("phoneNumber"),null=False, blank = False, unique = True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    #is_seller = models.BooleanField(null = True, default = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'nickname', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Area(models.Model):
    areaUser = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='areas')
    measuringInstrument = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text