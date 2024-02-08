
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    class Meta:
        app_label = 'property_management'

CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'
  

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    document_proofs = models.TextField()

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=50)
    features = models.TextField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    type_choices = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    ]
    unit_type = models.CharField(max_length=4, choices=type_choices)

    def __str__(self):
        return f"{self.property.name} - {self.get_unit_type_display()}"

class Tenant(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()

    def __str__(self):
        return f"{self.user_profile.user.email} - {self.unit.property.name} - {self.unit.get_unit_type_display()}"
