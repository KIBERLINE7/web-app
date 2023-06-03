from django.contrib import admin
from .models import Users
from .models import Department
from .models import Position_Empl
from .models import Tokens

admin.site.register(Users)
admin.site.register(Department)
admin.site.register(Position_Empl)
admin.site.register(Tokens)
