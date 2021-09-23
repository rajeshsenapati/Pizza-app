from django.contrib import admin
from .models import PizaModel, StorsModel, ReviewModel
# Register your models here.

admin.site.register(StorsModel)
admin.site.register(PizaModel)
admin.site.register(ReviewModel)