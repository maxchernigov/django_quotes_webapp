from django.db import models

class Authors(models.Model):
    fullname = models.CharField(max_length=25, null=False, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    
    def __str__(self):
        return f"{self.name}"


class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, default=None, null=False)
    quote = models.TextField()

    def __str__(self):
        return f"{self.tags}"
