# coding: utf-8
import os
from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import ugettext as _
from djangocms_text_ckeditor.fields import HTMLField
from cms.models import Page
from cms.models.pluginmodel import CMSPlugin
from PIL import Image
from cStringIO import StringIO


class Gallery(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('Name'))
    height = 0
    width  = 0

    def size(self):
        return (self.width, self.height)

    def copy_relations(self, oldinstance):
        for item in oldinstance.galleryitem_set.all():
            item.pk = None
            item.gallery = self
            item.save()

    def __unicode__(self):
        return self.domid


class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery)
    #caption_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)    
    caption_content = HTMLField(blank=True, null=True)    
    link_text = models.CharField( _("Text"), max_length=255, blank=True, help_text=_("Link text to display"))
    
    page_link = models.ForeignKey(
        Page, verbose_name=_("page"), null=True,
        limit_choices_to={'publisher_is_draft': True},
        help_text=_("If present, clicking on image will take user to "
                    "specified page."))    

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image.file)
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')

            if not (self.gallery.width <= 0 or self.gallery.height <= 0):
                img = img.resize(self.gallery.size(), Image.ANTIALIAS)

            temp_handle = StringIO()
            img.save(temp_handle, 'png')
            temp_handle.seek(0)

            suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                     temp_handle.read(),
                                     content_type='image/png')
            fname = "%s.png" % os.path.splitext(self.image.name)[0]
            self.image.save(fname, suf, save=False)

        super(GalleryItem, self).save()
