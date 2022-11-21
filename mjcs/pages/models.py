from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(config_name='default')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.SmallIntegerField(default=0)
    visibility = models.BooleanField(default=False)
    category = models.ForeignKey('PageCategory', on_delete=models.CASCADE, null=True)
    header_image = models.ImageField(upload_to='images/page_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, default=title)

    class Meta:
        ordering = ['order' ,'title']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

class PageCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    order = models.SmallIntegerField(default=0)
    menu_visibility = models.BooleanField(default=True)
    main_color = ColorField(default='#FF0000', format='hex')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Page Category'
        verbose_name_plural = 'Page Categories'

class PageImages(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/page_images/')
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page.title + self.name


    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Carrousel Image'
        verbose_name_plural = 'Carrousel Images'

class MainPage(Page):
    category = "Main Page"
    order = 0
    visibility = True

    class Meta:
        proxy = True
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Page'

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        super().save(*args, **kwargs)
