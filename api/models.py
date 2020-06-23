from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


# refer to Ghostpost models
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    post_type = models.BooleanField()
    post_key = models.CharField(
        max_length=6,
        blank=True,
        default=get_random_string(6).lower(),
        editable=False
    )

    # final_votes to sort by
    def post_votes(self):
        final_votes = self.upvotes - self.downvotes
        return final_votes

    def __str__(self):
        return self.title
