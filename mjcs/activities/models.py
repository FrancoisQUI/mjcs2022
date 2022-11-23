from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nom')
    description = RichTextUploadingField(config_name='default', verbose_name='Description')
    header_image = models.ImageField(upload_to='images/activity_images/',verbose_name='Image d\'en-tête')
    visibility = models.BooleanField(default=True, verbose_name='Visible')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    type = models.ForeignKey('ActivityType', on_delete=models.CASCADE, null=True, verbose_name='Type')
    slug = models.SlugField(max_length=200, unique=True, default=name, verbose_name='Slug')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Activité'
        verbose_name_plural = 'Activités'

class ActivityType(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nom')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type d\'activité'
        verbose_name_plural = 'Types d\'activités'


class ActivityPrice(models.Model):
    DURATION = [("YR", "Year"),("SE", "Semester"),("TR", "Trimester"),("MN", "Month")]


    activities = models.ManyToManyField(Activity, related_name='prices', verbose_name='Activités')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Prix')
    duration = models.CharField(max_length=2, choices=DURATION, default="SE", verbose_name='Durée')
    association_subscription = models.BooleanField(default=False, verbose_name='Abonnement association')
    note = models.CharField(max_length=200, verbose_name='Note', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')

    def __str__(self):
        return str(self.price) + "€ / " + self.duration +  " : " + self.note

    class Meta:
        verbose_name = 'Prix'
        verbose_name_plural = 'Prix'


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='images', verbose_name='Activité')
    image = models.ImageField(upload_to='images/activity_images/', verbose_name='Image')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class ActivitySession(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='sessions', verbose_name='Activité')
    day = models.TextField(choices=[("lun", "Lundi"),
                                    ("mar", "Mardi"),
                                    ("mer", "Mercredi"),
                                    ("jeu", "Jeudi"),
                                    ("ven", "Vendredi"),
                                    ("san", "Samedi"),
                                    ("dim", "Dimanche")],
                            default="lun",
                            verbose_name='Jour')
    start_time = models.TimeField(default="09:00", verbose_name='Heure de début')
    end_time = models.TimeField(default="10:00", verbose_name='Heure de fin')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de modification')
    age_min = models.IntegerField(default=0, verbose_name='Age minimum')
    age_max = models.IntegerField(default=99, verbose_name='Age maximum')

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'