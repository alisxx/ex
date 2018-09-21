from django.db import models
from django.utils.encoding import force_bytes

def __str__(self):
    return force_bytes(self.name)
# Create your models here.
def __unicode__(self):
    return self.name