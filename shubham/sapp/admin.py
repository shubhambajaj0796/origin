from django.contrib import admin

# Register your models here.
from sapp.models import web2
from sapp.models import news
from .models import tb_registration, emp_model

admin.site.register(web2)
admin.site.register(news)
admin.site.register(tb_registration)
admin.site.register(emp_model)