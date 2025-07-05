#imports
from django.contrib import admin
from content.models import *

#--------------------------------------------------------------------------------------------------
#model registration
admin.site.register(Post)
admin.site.register(Comment)