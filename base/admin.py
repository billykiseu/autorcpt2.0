from django.contrib import admin
from.models import Profile, CustomUser, category , workbook, Receipt, Email

# Register your models here.
admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(category)
admin.site.register(workbook)
admin.site.register(Receipt)
admin.site.register(Email)
