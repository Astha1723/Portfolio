from django.contrib import admin

# Register your models here.
from .models import Skill, Project, Contact

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)