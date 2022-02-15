from django.db import models

from users.models import Base, User

class Accommodation(Base):
    name           = models.CharField(max_length=250)
    description    = models.CharField(max_length=250)
    price          = models.DecimalField(decimal_places=2, max_digits=4)
    address        = models.CharField(max_length=250)
    region         = models.CharField(max_length=30)
    is_verified    = models.BooleanField(default=False)
    latitude       = models.CharField(max_length=100)
    longtitude     = models.CharField(max_length=100)
    check_in_time  = models.CharField(max_length=30)
    check_out_time = models.CharField(max_length=30)

    class Meta:
        db_table = 'accommodations'

class AccommodationImage(Base):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    image_url     = models.CharField(max_length=250)

class ThemaGroup(Base):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    type          = models.PositiveIntegerField()

    class Meta:
        db_table = 'thema_groups'

class Review(Base):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    comment       = models.CharField(max_length=250)
    score         = models.DecimalField(decimal_places=2, max_digits=3)

    class Meta:
        db_table = 'reviews'

class ReviewImage(Base):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=250)

    class Meta:
        db_table = 'review_images'
