from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    votes_total = models.IntegerField(default=1)

    pub_date_pretty = models.CharField()

    # Foreign key is id from other model
    # Foreign key points to User Id from User models (db)
    # if user deletes their account, also delete their products
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
