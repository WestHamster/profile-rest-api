from django.contrib import admin

from profile_api import models


admin.site.register(models.UserProfile)     #register the model UserProfile to make it accessible
# Register your models here.
