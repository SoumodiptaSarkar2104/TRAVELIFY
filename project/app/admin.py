from django.contrib import admin

# Register your models here.
from .models import Image, userdata
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']
@admin.register(userdata)
class userdataAdmin(admin.ModelAdmin):
    list_display=['id','Name','DOB','Email','Contact','Place','Gender','Country','Password']