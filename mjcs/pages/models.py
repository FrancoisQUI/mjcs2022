from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _



class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Titre'))
    content = RichTextUploadingField(config_name='default', verbose_name=_('Contenu'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de création'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Date de modification'))
    order = models.SmallIntegerField(default=0, verbose_name=_('Ordre'))
    visibility = models.BooleanField(default=False, verbose_name=_('Visibilité'))
    category = models.ForeignKey('PageCategory',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True,
                                 verbose_name=_('Catégorie'))
    header_image = models.ImageField(upload_to='images/page_images/',
                                     null=True,
                                     blank=True,
                                     verbose_name=_('Image d\'en-tête'))
    slug = models.SlugField(max_length=200, unique=True, default=title, verbose_name=_('Slug'))

    class Meta:
        ordering = ['order' ,'title']
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[self.slug])

class PageCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nom'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    order = models.SmallIntegerField(default=0, verbose_name=_('Ordre'))
    menu_visibility = models.BooleanField(default=True, verbose_name=_('Visibilité dans le menu'))
    main_color = ColorField(default='#FF0000', format='hex', verbose_name=_('Couleur principale'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Catégorie de page')
        verbose_name_plural = _('Catégories de page')

class PageImages(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images', verbose_name=_('Page'))
    image = models.ImageField(upload_to='images/page_images/', verbose_name=_('Image'))
    name = models.CharField(max_length=200, verbose_name=_('Nom'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date de création'))
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_('Date de modification'))

    def __str__(self):
        return self.page.title + self.name


    def __int__(self):
        return self.id

    class Meta:
        verbose_name = _('Image pour Carrousel')
        verbose_name_plural = _('Images du Carrousel')

class MainPage(Page):
    category = "Main Page"
    order = 0
    visibility = True

    class Meta:
        proxy = True
        verbose_name = _('Page Principale')
        verbose_name_plural = _('Pages Principales')

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        super().save(*args, **kwargs)
