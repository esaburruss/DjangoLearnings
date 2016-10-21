from django.contrib import admin
from pages.models import Section, Page
from alumni.models import Brother, Exec
from image.models import ImageUpload

admin.site.register(Section)
admin.site.register(Page)
admin.site.register(ImageUpload)
admin.site.register(Brother)
admin.site.register(Exec)