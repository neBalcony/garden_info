from django.db import models
from django.utils.text import slugify

class Card(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class NFCTag(models.Model):
    uid = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(max_length=200, blank=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='nfc_tags')

    def __str__(self):
        return f"{self.card.slug}"
