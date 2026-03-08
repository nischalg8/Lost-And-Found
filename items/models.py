from django.db import models
from django.conf import settings

class Item(models.Model):
    
    STATUS_CHOICE = (
        ('claimed','Claimed'),
        ('not_claimed', 'Not Claimed')             
    )
    
    POST_TYPE = (
        ('lost', 'Lost Post'),
        ('found', 'Found Post'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    date_found = models.DateField()
    location = models.CharField(max_length=100)
    found_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField('item_image', upload_to='images/')
    status = models.CharField(choices=STATUS_CHOICE, default='not_claimed')
    post_type = models.CharField(max_length=10, choices=POST_TYPE, default='lost')

    def __str__(self):
        return self.name