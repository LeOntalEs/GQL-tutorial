from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    list_filter = ('name',)
    search_fields = ('name',)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Borrow._meta.fields]
    list_filter = ('doc__category', 'borrow_time', 'return_time')
    search_fields = ('doc__category', 'doc', 'borrow_time', 'return_time')
class DocumentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Document._meta.fields]
    list_display = ('title', 'category')
    search_fields =  ('title', 'category')

admin.site.register(Document, DocumentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Borrow, BorrowAdmin)
