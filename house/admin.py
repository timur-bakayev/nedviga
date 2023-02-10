from django.contrib import admin
from .models import *
from .base_model import *

admin.site.register(House)
admin.site.register(Kvartira)
admin.site.register(Dacha)
admin.site.register(BaseModel)
