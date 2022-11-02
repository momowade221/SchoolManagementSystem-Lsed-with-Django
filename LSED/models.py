from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name.upper()
    class Meta:
        verbose_name='Professeur'


classes=[('Seconde','Seconde'),('Première','Première'),('Terminale','Terminale')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name.upper()
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    class Meta:
        verbose_name = 'Elève'


class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)
    class Meta:
        verbose_name = 'Présence'


class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.TextField()
    class Meta:
        verbose_name = 'Notification'