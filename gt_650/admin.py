from django.contrib import admin
from .models import student
# Register your models here.
admin.site.site_header = "prabhat"
admin.site.site_title = "prabhat"
admin.site.index_title = "prabhat"

class modelAdmin(admin.ModelAdmin):
    list_display=('email','password')

admin.site.register(student,modelAdmin)