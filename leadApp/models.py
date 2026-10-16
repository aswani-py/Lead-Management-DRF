from django.db import models

# Create your models here.

class Lead(models.Model):
    SOURCE_CHOICES=(
        ("walk-in","walk-in"),
        ("call","call"),
        ("referral","referral"),
        ("website","website")
    )
    STATUS_CHOICES=(
            ("New","New"),
            ("Contacted","Contacted"),
            ("Converted","Converted"),
            ("Lost","Lost")
        )

    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    source=models.CharField(max_length=100,choices=SOURCE_CHOICES)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES)
    added_date=models.DateTimeField(auto_now=True)
    notes=models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return f"{self.name} - {self.phone}"


