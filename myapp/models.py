from django.db import models

class Student(models.Model):
    name = models.CharField(max_length= 50)
    f_name = models.CharField(max_length=60)
    roll_no = models.IntegerField()
    marks = models.IntegerField()
    # admission_date = models.DateTimeField()
    # pass_date = models.DateField()


    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length= 50)
    emp_id= models.IntegerField()
    salaty = models.IntegerField()
    join_date = models.DateField()

    def __str__(self):
        return self.name
            

# Create your models here.
