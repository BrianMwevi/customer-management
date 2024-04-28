from django.db import models


class TimeStamped(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
