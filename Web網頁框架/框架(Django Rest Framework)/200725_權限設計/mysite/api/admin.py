from django.contrib import admin
from api import models


admin.site.register(models.User)
admin.site.register(models.Role)
admin.site.register(models.UserRole)
admin.site.register(models.Permission)
admin.site.register(models.RolePermission)
