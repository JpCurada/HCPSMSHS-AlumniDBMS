from django.db import models

class Record(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=5)
    sex = models.CharField(max_length=5)
    strand = models.CharField(max_length=10)
    graduation_year = models.IntegerField()
    college_university = models.CharField(max_length=100)
    college_course = models.CharField(max_length=100)
    hei = models.CharField(max_length=10)

    def __str__(self):
        return(f"{self.last_name}, {self.first_name} {self.middle_initial}")
    
    

