from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=255, blank=True)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.text
        
    
