from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Product, Marka, AboutPage, Gallery, Year
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


class MarkaAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    prepopulated_fields = {'url': ('name',)} 


class YearAdmin(admin.ModelAdmin):
    list_display = ['year', 'url']
    prepopulated_fields = {'url': ('year',)} 


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'marka', 'year', 'price']
    prepopulated_fields = {'url': ('name',)} 
    save_on_top = True

admin.site.register(Product, ProductAdmin)
admin.site.register(Marka,MarkaAdmin)
admin.site.register(Year,YearAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
