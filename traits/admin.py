from django.contrib import admin
from .models import Trait, Publocal

class TraitInline(admin.TabularInline):
    model = Trait
    show_change_link = True

class PublocalAdmin(admin.ModelAdmin):
    inlines = [
        TraitInline,
    ]

admin.site.register(Trait)
admin.site.register(Publocal, PublocalAdmin)
