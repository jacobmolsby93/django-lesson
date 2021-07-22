from django.db import models

# Create your models here.
# When creating this item, django will automatically create a table for this class in the database.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
