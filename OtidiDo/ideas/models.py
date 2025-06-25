from django.db import models

from OtidiDo.accounts.models import Traveler


# Create your models here.
class Idea(models.Model):
    CATEGORY_CHOICES = [
        ('nature', 'Природа'),
        ('urban', 'Градско'),
        ('event', 'Събитие')
    ]

    user = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='ideas')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='ideas/', blank=True, null=True)
    city = models.CharField(max_length=100)
    date_event = models.DateField(blank=True, null=True) #Само за събития
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'idea')


class Comment(models.Model):
    user = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
