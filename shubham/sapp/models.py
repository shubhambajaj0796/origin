from django.db import models

# Create your models here.
class web2(models.Model):
    news_head = models.CharField(max_length=225)
    news_web = models.CharField(max_length=225)
    date = models.DateField()

class news(models.Model):
    title = models.CharField(max_length=225)
    authors = models.CharField(max_length=225)
    publisher = models.ForeignKey(web2,on_delete=models.PROTECT)
    publication_date = models.DateField()

class tb_registration(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

class emp_model(models.Model):
    e_salary = models.CharField(max_length=225)
    e_experience = models.CharField(max_length=225)
    e_profile = models.CharField(max_length=225)
    e_detail = models.ForeignKey(tb_registration,on_delete=models.PROTECT)


