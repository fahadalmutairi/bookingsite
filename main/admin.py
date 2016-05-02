from django.contrib import admin
from main.models import Property, Rating, Schedule, Address, Amenities, PropertyImages, CustomUser
# Register your models here.

admin.site.register(Property)
admin.site.register(Rating)
admin.site.register(Schedule)
admin.site.register(Address)
admin.site.register(Amenities)
admin.site.register(PropertyImages)
admin.site.register(CustomUser)
