from django.db import models 
from django.db.models import Model 
from jsonfield import JSONField

  
class url(Model): 
    url_nm = models.URLField(max_length = 200,primary_key=True)
    res = JSONField()
def __str__(self):
       return self.name
