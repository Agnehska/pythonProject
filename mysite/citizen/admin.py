from django.contrib import admin
from .models import *

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'age', 'status')

admin.site.register(People, PeopleAdmin)
admin.site.register(Status)