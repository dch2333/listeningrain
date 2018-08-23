from django.db import models

# Create your models here.


class Rain(models.Model):
    title = models.CharField(max_length=20, verbose_name=u"标题")
    content = models.CharField(max_length=100, verbose_name=u'内容')
    def __unicode__(self):
    	return self.title