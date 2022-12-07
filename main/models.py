from django.db import models


class About(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.name


class What(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title


class Categoriya(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Project(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')





class Post(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    text = models.TextField()
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# Create your models here.
