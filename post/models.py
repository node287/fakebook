from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_date = models.DateTimeField()
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'postImages/')
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag[:10]

    def formatDate(self):
        return self.post_date.strftime("%b %e %Y")