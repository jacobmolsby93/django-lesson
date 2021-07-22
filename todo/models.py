from django.db import models

# Create your models here.
# When creating this item, django will automatically create a
#  table for this class in the database.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # overrides the str method of how our items are displaced,
    # str method is defines in django.db
    def __str__(self):
        return self.name
