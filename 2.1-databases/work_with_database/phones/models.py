from django.db import models


class Phone(models.Model):
    name = models.CharField()
    price = models.CharField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
