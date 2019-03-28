from django.contrib import admin
from .models import Trait, Publocal

class TraitInline(admin.TabularInline):
    model = Trait
    show_change_link = True

class PublocalAdmin(admin.ModelAdmin):
    inlines = [
        TraitInline,
    ]

class TraitAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pubref')

admin.site.register(Trait, TraitAdmin)
admin.site.register(Publocal, PublocalAdmin)
