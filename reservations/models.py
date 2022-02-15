from tkinter import CASCADE
import uuid

from django.db import models

from users.models import Base, User
from accommodations.models import Accommodation

class Reservation(Base):
    user               = models.ForeignKey(User, on_delete=CASCADE)
    accommodation      = models.ForeignKey(Accommodation, on_delete=CASCADE)
    check_in           = models.DateTimeField()
    check_out          = models.DateTimeField()
    number_of_adults   = models.PositiveIntegerField(default=1)
    number_of_children = models.IntegerField(default=0)
    reservation_code   = models.UUIDField(default=uuid.uuid4)

    class Meta:
        db_table = 'reservations'
