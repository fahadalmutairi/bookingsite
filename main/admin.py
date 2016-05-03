from django.contrib import admin
from main.models import Property, Rating, Schedule, Address, Amenities, PropertyImages, CustomUser, Booking , Schedule_2

# Register your models here.
class PropertyInline(admin.StackedInline):
    model = Property

class AddressAdmin(admin.ModelAdmin):
    inlines = [PropertyInline,]
admin.site.register(Property)
admin.site.register(Rating)
admin.site.register(Schedule)
admin.site.register(Address, AddressAdmin)
admin.site.register(Amenities)
admin.site.register(PropertyImages)
admin.site.register(CustomUser)
admin.site.register(Booking)

