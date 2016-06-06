# coding=utf-8
from django.contrib import admin

from perfect_space.apps.publications.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title_ru', 'description_ru',)
    readonly_fields = ('preview_cover',)

    fieldsets = [
        (None, {
            'fields': ['file', 'cover', 'preview_cover']
        }),
        ('Русский', {
            'fields': ['title_ru', 'description_ru']}),
        ('Английский', {
            'fields': ['title_en', 'description_en']}),
    ]
admin.site.register(Publication, PublicationAdmin)
