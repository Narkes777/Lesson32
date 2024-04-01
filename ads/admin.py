from django.contrib import admin
from .models import Ad, Category, Author

# Register your models here.

admin.site.register(Ad)
admin.site.register(Author)
admin.site.register(Category)
