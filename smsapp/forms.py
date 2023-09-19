from django import forms

class regform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    fname=forms.CharField(max_length=20)
    mname=forms.CharField(max_length=20)
    no=forms.CharField(max_length=20)
    cls=forms.CharField(max_length=20)
    adrs=forms.CharField(max_length=50)
    pas=forms.CharField(max_length=20)
    con=forms.CharField(max_length=20)

class logform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)

class registerform(forms.Form):
    
    email=forms.EmailField()
    no=forms.CharField(max_length=20)
    cls=forms.CharField(max_length=20)
    pas=forms.CharField(max_length=20)
    con=forms.CharField(max_length=20)

class loginform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)

class asgmntform(forms.Form):
    cl=forms.CharField(max_length=20)
    sub=forms.CharField(max_length=20)
    asno=forms.CharField(max_length=20)
    dd=forms.CharField(max_length=20)
    ass=forms.FileField()

class subasgform(forms.Form):
    name=forms.CharField(max_length=20)
    clas=forms.CharField(max_length=20)
    sbjt=forms.CharField(max_length=20)
    no=forms.CharField(max_length=20)
    asmnt=forms.FileField()

class reviewform(forms.Form):
    name=forms.CharField(max_length=20)
    clas=forms.CharField(max_length=20)
    tl=forms.CharField(max_length=20)
    cca=forms.CharField(max_length=20)
    ps=forms.CharField(max_length=20)
    hf=forms.CharField(max_length=20)
    it=forms.CharField(max_length=20)
    ct=forms.CharField(max_length=20)
    cf=forms.CharField(max_length=20)
    ll=forms.CharField(max_length=20)
    sg=forms.CharField(max_length=50)


class pnotesform(forms.Form):
    cl=forms.CharField(max_length=20)
    sub=forms.CharField(max_length=20)
    chno=forms.CharField(max_length=20)
    note=forms.FileField()
    


