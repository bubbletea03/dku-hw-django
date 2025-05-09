from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_detail = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.project_detail


class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.IntegerField()