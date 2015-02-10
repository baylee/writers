from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)
    twitter = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return u"{}".format(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return u"{}".format(self.name)