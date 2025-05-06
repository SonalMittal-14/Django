from django.db import models
# Models define your Database.


# makemigration => create changes and store them in a file
# migrate => apply the pending changes created by makemigration

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    subject = models.TextField()
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name  


#models ke anadr jo bhi h vo ek tarah se table h database mai 
#jese contact agar table h toh name,email,phone etc columns h
# python manage.py makemigrations ka ye mtlb hai ki mai apnai django ko ye bta rahi hu ki django mene kuch chnages kiye h apnai model mai zara un changes ki file bna lo