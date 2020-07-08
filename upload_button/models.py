from django.db import models

class UploadedContent(models.Model):
    user=models.CharField(max_length=150)
    caption =models.TextField()
    post=models.ImageField()
    datetime=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user
