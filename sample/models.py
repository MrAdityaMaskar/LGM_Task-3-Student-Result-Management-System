from django.db import models

# Create your models here.
# create table DemoTable729 (
''' StudentId int NOT NULL AUTO_INCREMENT PRIMARY KEY,
   StudentName varchar(100),
   MySQLMarks int,
   CMarks int,
   JavaMarks int
);'''


class StudentList(models.Model):
    student_name = models.CharField(max_length=200)
    course = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200,  null=True)
    address = models.TextField(default='Something')

    def __str__(self):
        return self.student_name


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.ForeignKey(StudentList, on_delete=models.CASCADE)

    DBMS = models.FloatField()
    CNS = models.FloatField()
    SPOS = models.FloatField()
    IOTES = models.FloatField()
    TOC = models.FloatField()
    aggregate = models.FloatField()
    Total = models.FloatField()

    def __str__(self):
        return self.student_name.student_name




