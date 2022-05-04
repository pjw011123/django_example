from django.contrib import admin
from first_app.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
print(1)
# Register your models here.
