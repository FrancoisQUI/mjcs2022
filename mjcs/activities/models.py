from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    header_image = models.ImageField(upload_to='images/activity_images/')
    visibility = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('ActivityType', on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200, unique=True, default=name)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'

class ActivityType(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activity Types'


class ActivityPrice(models.Model):
    activities = models.ManyToManyField(Activity, related_name='prices')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/activity_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class ActivitySession(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='sessions')
    day = models.TextField(choices=[("lun", "Lundi"),
                                    ("mar", "Mardi"),
                                    ("mer", "Mercredi"),
                                    ("jeu", "Jeudi"),
                                    ("ven", "Vendredi"),
                                    ("san", "Samedi"),
                                    ("dim", "Dimanche")],
                            default="lun")
    start_time = models.TimeField(default="09:00")
    end_time = models.TimeField(default="10:00")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    session_quantity = models.IntegerField(default=1)
    session_age_min = models.IntegerField(default=0)
    session_age_max = models.IntegerField(default=99)