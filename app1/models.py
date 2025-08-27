from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Movie(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/',null=True, blank=True)
    genre=models.CharField(max_length=50)
    actor=models.ManyToManyField('Actor')

    def __str__(self):
        return self.name


class Actor(models.Model):
    name=models.CharField(max_length=150)
    birthdate=models.DateField()

    def __str__(self):
        return self.name

class CommitMovie(models.Model):
    title=models.CharField(max_length=50)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    create_ed=models.DateField(auto_now_add=True)
    update_ed=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.create_ed}-{self.update_ed}"

