from django.contrib import admin
from .models import *
# Register your models here.

# class test_tblAdmin(admin.ModelAdmin):
#     # 列表页属性
#     list_display = ['pk', 'name', 'date',  'tem', 'Delete']
#     list_filter = ['name']
#     search_fields = ['name']
#     list_per_page = 4
#     # # 添加，修改页属性
#     fields = ['tem','name', 'date', 'Delete']
#     fieldsets = [
#         ("num", {"fields": ['tem']}),
#         ("base", {"fields": ["name", "date", "Delete"]}),
#     ]


admin.site.register(s821)

