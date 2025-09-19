from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class NFCTag(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='nfc_tags')

    def __str__(self):
        return f"{self.card.title}"
