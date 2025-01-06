from django.db import models

# Create your models here.
class Feed(models.Model):
    user=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    pic=models.ImageField(upload_to="media",null=True)
    caption=models.CharField(max_length=200)


    def __str__(self):
        return self.user
