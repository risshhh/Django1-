from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=200)
	std = models.CharField(max_length=200)
	college = models.CharField(max_length=200)
	branch = models.CharField(max_length=200)


	def __str__(self):
		return self.name


class Student(models.Model):
	name = models.CharField(max_length=200)
	regno = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)

	def __str__(self):
		return self.name
