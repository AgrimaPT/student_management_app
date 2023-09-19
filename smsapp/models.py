from django.db import models

# Create your models here.
c=[('8','8'),('9','9'),('10','10')]
class regmodel(models.Model):
    nm=models.CharField(max_length=20)
    eml=models.EmailField()
    fnm=models.CharField(max_length=20)
    mnm=models.CharField(max_length=20)
    num=models.CharField(max_length=20)
    cl=models.CharField(max_length=20,choices=c)
    adr=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

cl=[('8','8'),('9','9'),('10','10')]
class registermodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    numb=models.CharField(max_length=20)
    clss=models.CharField(max_length=20,choices=cl)
    pswd=models.CharField(max_length=20)

class asgmntmodel2(models.Model):
    cla=models.CharField(max_length=20)
    su=models.CharField(max_length=20)
    ano=models.CharField(max_length=20)
    due=models.CharField(max_length=20)
    asg=models.ImageField(upload_to="smsapp/static")

class subasgmodel(models.Model):
    name=models.CharField(max_length=20)
    cla=models.CharField(max_length=20)
    sb=models.CharField(max_length=20)
    numb=models.CharField(max_length=20)
    asg=models.ImageField(upload_to="smsapp/static")

a=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
b=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
c=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
d=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
e=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
f=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
g=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
h=[('Excellent','Excellent'),('Very good','Very good'),('Good','Good'),('Average','Average'),('Poor','Poor')]
class reviewmodel(models.Model):
    nm=models.CharField(max_length=20)
    cl=models.CharField(max_length=20)
    tlm=models.CharField(max_length=20,choices=a)
    ccam=models.CharField(max_length=20,choices=b)
    psm=models.CharField(max_length=20,choices=c)
    hfm=models.CharField(max_length=20,choices=d)
    itm=models.CharField(max_length=20,choices=e)
    ctm=models.CharField(max_length=20,choices=f)
    cfm=models.CharField(max_length=20,choices=g)
    llm=models.CharField(max_length=20,choices=h)
    sgm=models.CharField(max_length=100)
    

class pnotesmodel(models.Model):
    cla=models.CharField(max_length=20)
    su=models.CharField(max_length=20)
    cno=models.CharField(max_length=20)
    nt=models.ImageField(upload_to="smsapp/static")


