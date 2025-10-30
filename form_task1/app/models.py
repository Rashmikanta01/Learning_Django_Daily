from django.db import models


# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    # keep original attribute name used by views/templates
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='webpages')
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    # restore original FK name `name` so existing views/templates keep working
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE, related_name='access_records')
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.author


