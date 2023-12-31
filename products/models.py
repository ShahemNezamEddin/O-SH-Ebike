from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    motor = models.CharField(max_length=254, null=True, blank=True)
    speed = models.CharField(max_length=254, null=True, blank=True)
    battery = models.CharField(max_length=254, null=True, blank=True)

    brake = models.CharField(max_length=254, null=True, blank=True)
    frame = models.CharField(max_length=254, null=True, blank=True)
    tires = models.CharField(max_length=254, null=True, blank=True)
    range_pas_mode = models.CharField(max_length=254, null=True, blank=True)
    range_electric_mode = models.CharField(max_length=254, null=True, blank=True)
    gross_weight = models.CharField(max_length=254, null=True, blank=True)
    bike_weight = models.CharField(max_length=254, null=True, blank=True)
    charging_time = models.CharField(max_length=254, null=True, blank=True)
    display = models.CharField(max_length=254, null=True, blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_1_url = models.URLField(max_length=1024, null=True, blank=True)
    image_1 = models.ImageField(null=True, blank=True)
    image_tires_url = models.URLField(max_length=1024, null=True, blank=True)
    image_tires = models.ImageField(null=True, blank=True)
    image_brake_url = models.URLField(max_length=1024, null=True, blank=True)
    image_brake = models.ImageField(null=True, blank=True)
    image_display_url = models.URLField(max_length=1024, null=True, blank=True)
    image_display = models.ImageField(null=True, blank=True)
    image_gears_url = models.URLField(max_length=1024, null=True, blank=True)
    image_gears = models.ImageField(null=True, blank=True)
    image_safety_url = models.URLField(max_length=1024, null=True, blank=True)
    image_safety = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name