from cProfile import Profile
from django.db import models
from django.db.models.signals import post_save ,pre_delete
from django.dispatch import receiver
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.conf import settings


#Custom user and profile stuff
class CustomUser(AbstractUser):
    # Define user roles as constants
    SUPERUSER = 'superuser'
    USER = 'user' 

    ROLE_CHOICES = (
        (SUPERUSER, 'superuser'),
        (USER, 'user'),
    )

    role = models.CharField(max_length=50, default=USER, choices=ROLE_CHOICES)
    
    #avoiding naming conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='media', blank=True, default='profile/default.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profilepic.path)
        if img.height > 100 or img.width > 100:
            new_img_size = (300, 300)
            img.thumbnail(new_img_size)
            img.save(self.profilepic.path)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance:
        try:
            profile = instance.profile
        except Profile.DoesNotExist:
            profile = None
        if not profile:
            Profile.objects.create(user=instance)
            
@receiver(pre_delete, sender=CustomUser)
def delete_user_profile(sender, instance, **kwargs):
    try:
        profile = instance.profile
        profile.delete()
    except Profile.DoesNotExist:
        pass

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

#document models
class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class workbook(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('pending', 'Pending')
    )
    category = models.ForeignKey(
        category, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='files', blank=True)  # Changed to FileField
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', blank=True)

    def __str__(self):
        return self.name
    
    #keeping things clean
    def save(self, *args, **kwargs):
        try:
            this = workbook.objects.get(id=self.id)
            if this.file != self.file:
                this.file.delete(save=False)
        except:
            pass
        super().save(*args, **kwargs)

#Receipts
class Receipt(models.Model):
    receipt_number = models.CharField(max_length=20, unique=True)
    house_number = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pending = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.receipt_number
    
    @property
    def formatted_phone(self):
        # Remove the leading "254" and add "0" as the prefix
        return "0" + self.phone[3:]
    
    def get_emails(self):
        # Retrieve all associated emails and join them with commas
        emails = self.email_set.values_list('address', flat=True)
        return ', '.join(emails)

#emails
class Email(models.Model):
    address = models.EmailField()
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.address


  