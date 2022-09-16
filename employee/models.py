from email.policy import default
from enum import unique
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
from django.db import models  
#from datetime import datetime

#using abstract and base class
class common(models.Model):
    eemail = models.EmailField()
    
    class Meta:
        abstract = True
        
class Employee(common):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
 #   date = models.DateTimeField(default=datetime.now,blank=True)
  
    #slug = models.SlugField(null=True)  # new

    
    #new_slug=AutoSlugField(populate_from='email',unique=True,null=True,default=None)
    def get_absolute_url(self):
        return reverse("emp_detail", kwargs={"slug": self.slug})
    
    class Meta:  
        indexes = [models.Index(fields=['ename','eemail'])]
        db_table = "employee"  
        verbose_name_plural = "employee"
        #using unique constraints
        constraints = [models.UniqueConstraint(fields=['eid'], name= 'unique_id')]
        
        
class Department(common):
    eemail = models.EmailField()
    
   

    
        

