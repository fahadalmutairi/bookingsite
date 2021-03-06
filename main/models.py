from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



# Create your models here.

class Property(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	bedrooms = models.IntegerField(null=True,blank=True)
	floors = models.IntegerField()
	address = models.ForeignKey('main.Address', blank=True, null=True)
	rate_by_day = models.IntegerField(blank=True, null=True)
	rate_by_week = models.IntegerField(blank=True, null=True)
	owner = models.ForeignKey('main.CustomUser')
	amenities = models.ManyToManyField('main.Amenities')
	longitude = models.FloatField()
	latitude = models.FloatField()
	PROPERTY_TYPE_CHOICES =(
		('Apartment', 'Apartment'),
		('Chalet', 'Chalet'), 
        ('Farm', 'Farm'),
		)
	property_type_choices = models.CharField(choices=PROPERTY_TYPE_CHOICES, default='Farm', max_length=255)

	def __unicode__(self):
		return "%s" %self.name


class Schedule_2(models.Model):
    Rdate = models.DateField()
    Unavaliable = models.BooleanField(default=False)
    booked = models.BooleanField(default=False)
    property_o = models.ForeignKey('main.Property')
    def __unicode__(self):
        return "%s ,  %s" %(self.property_object , self.Rdate)

# ----- depreciated model please ignore
# class Type(models.Model):
#     propertytype = models.CharField(max_length=10)
#     property_object = models.ForeignKey('main.Property')

#     def __unicode__(self):
#         return "%s" % self.property_object

class Rating(models.Model):
	rating_by_user = models.IntegerField()
	property_object = models.ForeignKey('main.Property')
	user = models.ForeignKey('main.CustomUser')
	def __unicode__(self):
		return "%s by %s" %(self.property_object,self.user)

class Schedule(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    owner = models.ForeignKey('main.CustomUser')
    #user = models.ForeignKey('main.CustomUser',blank=True, null=True, related_name='user')
    # booked = models.BooleanField(default=False)
    property_object = models.ForeignKey('main.Property')
    def __unicode__(self):
        return "property: %s start date: %s end date: %s" %(self.property_object, self.date_start, self.date_end)

class Booking(models.Model):
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    owner = models.ForeignKey('main.CustomUser', related_name='owner', null=True, blank=True)
    user = models.ForeignKey('main.CustomUser',blank=True, null=True, related_name='user')
    booked = models.BooleanField(default=False)
    property_object = models.ForeignKey('main.Property', null=True, blank=True)
    schedule = models.ForeignKey('main.Schedule', null=True, blank=True)


    def __unicode__(self):
        return "start:%s end:%s by: %s" % (self.date_start, self.date_end, self.user)


class Address(models.Model):
	country = models.CharField(max_length=255)
	governorate = models.CharField(max_length=255)
	area = models.CharField(max_length=255)
	def __unicode__(self):
		return "%s" %self.area

class Amenities(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	icon = models.ImageField(upload_to='amenities_icons', null=True, blank=True)
	def __unicode__(self):
		return "%s" %self.name

class PropertyImages(models.Model):
	property_object = models.ForeignKey('main.Property')
	image = models.ImageField(upload_to='property_images')
	def __unicode__(self):
		return "image: %s" %self.property_object


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_owner,is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
        					is_owner=is_owner,
                            is_staff=is_staff,
                            is_active=True,
                            is_superuser=is_superuser,
                            last_login=now,
                            date_joined=now,
                            **extra_fields
                            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password,False, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password,True, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=255, blank=True, null=True)
    last_name = models.CharField('last name', max_length=255, blank=True, null=True)
    is_owner =  models.BooleanField('owner status', default=False)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return '/users/%s' % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject,message,from_email, [self.email])




