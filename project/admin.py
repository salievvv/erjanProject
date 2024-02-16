from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Product, Marka, AboutPage, Gallery
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AboutAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = AboutPage
        fields = '__all__'

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class AboutPageAdmin(admin.ModelAdmin): 
    list_display = ("title", "desc",)
    form = AboutAdminForm
    inlines = [GalleryInline,]

admin.site.register(Product)
admin.site.register(Marka)
admin.site.register(AboutPage, AboutPageAdmin)
