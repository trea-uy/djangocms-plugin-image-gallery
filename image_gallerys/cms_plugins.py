# coding: utf-8
import re
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *
from django.utils.translation import ugettext as _
from django.contrib import admin
from django.forms import ModelForm, ValidationError


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery

    def clean_domid(self):
        data = self.cleaned_data['domid']
        if not re.match(r'^[a-zA-Z_]\w*$', data):
            raise ValidationError(
                _("The name must be a single word beginning with a letter"))
        return data


class GalleryItemInline(admin.TabularInline):
    model = GalleryItem


class GalleryPlugin(CMSPluginBase):
    model = Gallery
    form = GalleryForm
    name = _("Gallery")
    render_template = "gallery.html"

    inlines = [
        GalleryItemInline,
        ]

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(GalleryPlugin)
