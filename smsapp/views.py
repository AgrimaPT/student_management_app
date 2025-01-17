from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def reg(request): 
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            nam=a.cleaned_data['name']
            emai=a.cleaned_data['email']
            fnam=a.cleaned_data['fname']
            mnam=a.cleaned_data['mname']
            numb=a.cleaned_data['no']
            clas=a.cleaned_data['cls']
            addr=a.cleaned_data['adrs']
            pwd=a.cleaned_data['pas']
            cpas=a.cleaned_data['con']
            if pwd==cpas:
                b=regmodel(nm=nam,eml=emai,fnm=fnam,mnm=mnam,num=numb,cl=clas,adr=addr,password=pwd)
                b.save()
                return redirect(log)
            else:
                return HttpResponse("password don't match")
        else:
            print(a.errors.as_data())
        # else:
        #     return HttpResponse("enter valid data")
    return render(request,'reg.html')

def log(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            pas=a.cleaned_data['pas']
            b=regmodel.objects.all()
            for i in b:
                if em==i.eml and pas==i.password:
                    name=i.nm
                    eml=i.eml
                    fnm=i.fnm
                    mnm=i.mnm
                    mob=i.num
                    cls=i.cl
                    adr=i.adr
                    id1=i.id
                    return render(request,'students.html',{'name':name,'eml':eml,'fnm':fnm,'mnm':mnm,'mob':mob,'cls':cls,'adr':adr,'id':id1})
            else:
                return HttpResponse("login failed...")
        else:
            return HttpResponse("enter valid details...")
    return render(request,'log.html')

def edit(request,id):
    user=regmodel.objects.get(id=id)
    if request.method=='POST':
        user.nm=request.POST.get('name')
        user.eml=request.POST.get('email')
        user.fnm=request.POST.get('fnm')
        user.mnm=request.POST.get('mnm')
        user.num=request.POST.get('no')
        user.cl=request.POST.get('cls')
        user.adr=request.POST.get('adr')
        user.save()
        return redirect(log)
    return render(request,'edit.html',{'user':user})

def register(request): 
    if request.method=='POST':
        a=registerform(request.POST)
        if a.is_valid():
            
            emai=a.cleaned_data['email']
            numb=a.cleaned_data['no']
            clas=a.cleaned_data['cls']
            pwd=a.cleaned_data['pas']
            cpas=a.cleaned_data['con']
            if pwd==cpas:
                b=registermodel(email=emai,numb=numb,clss=clas,pswd=pwd)
                b.save()
                return redirect(login)
            else:
                return HttpResponse("password don't match")
        else:
            print(a.errors.as_data())
        # else:
        #     return HttpResponse("enter valid data")
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            pas=a.cleaned_data['pas']
            b=registermodel.objects.all()
            for i in b:
                if em==i.email and pas==i.pswd:
                    cl=i.clss
                    id1=i.id
                    return render(request,'techers.html',{'c':cl,'id':id1})
            else:
                return HttpResponse("login failed...")
        else:
            return HttpResponse("enter valid details...")
    return render(request,'login.html')

def stu(request,id):
    obj=registermodel.objects.get(id=id)
    cls=obj.clss
    a=regmodel.objects.filter(cl=cls)
    return render(request,'stu.html',{'ts':a})

def asgmnt(request,id):
    obj=registermodel.objects.get(id=id)
    if request.method=='POST':
        a=asgmntform(request.POST,request.FILES)
        if a.is_valid():
            sub=a.cleaned_data['sub']
            asno=a.cleaned_data['asno']
            ass=a.cleaned_data['ass']
            dd=a.cleaned_data['dd']
            cl=a.cleaned_data['cl']

            
            b=asgmntmodel2(cla=cl,su=sub,ano=asno,asg=ass,due=dd)
            b.save()
            return HttpResponse("posted successfully")
        else:
           return HttpResponse("error") 
    return render(request,'asgmnt.html',{'c':obj})

def stuasg(request,id):
    obj=regmodel.objects.get(id=id)
    cls=obj.cl
    user=id
    a=asgmntmodel2.objects.filter(cla=cls)
    return render(request,'stuasg.html',{'ab':a,'user':user})

def subasg(request,id1,id2):
    obj=regmodel.objects.get(id=id2)
    nm=obj.nm
    cls=obj.cl
    a=asgmntmodel2.objects.get(id=id1)
    su=a.su
    ano=a.ano
    if request.method=='POST':
        a=subasgform(request.POST,request.FILES)
        if a.is_valid():
            name=a.cleaned_data['name']
            cls=a.cleaned_data['clas']
            sub=a.cleaned_data['sbjt']
            asno=a.cleaned_data['no']
            asm=a.cleaned_data['asmnt']
            
            
            b=subasgmodel(name=name,cla=cls,sb=sub,numb=asno,asg=asm)
            b.save()
            return HttpResponse("Submitted successfully")
        else:
           return HttpResponse("error") 
    return render(request,'subasg.html',{'su':su,'ano':ano,'nm':nm,'cls':cls})

def viewasg(request,id):
    obj=registermodel.objects.get(id=id)
    cls=obj.clss
    a=asgmntmodel2.objects.filter(cla=cls)
    
    return render(request,'viewasg.html',{'a':a})

def sbjtasg(request,id):

    obj=asgmntmodel2.objects.get(id=id)
    s=obj.su
    n=obj.ano
    a=subasgmodel.objects.filter(sb=s,numb=n)
    return render(request,'sbjtasg.html',{'a':a})

def review(request,id):

    obj=regmodel.objects.get(id=id)
    n=obj.nm
    cl=obj.cl
    if request.method=='POST':
        a=reviewform(request.POST)
        if a.is_valid():
            name=a.cleaned_data['name']
            cls=a.cleaned_data['clas']
            tl=a.cleaned_data['tl']
            cca=a.cleaned_data['cca']
            ps=a.cleaned_data['ps']
            hf=a.cleaned_data['hf']
            it=a.cleaned_data['it']
            ct=a.cleaned_data['ct']
            cf=a.cleaned_data['cf']
            ll=a.cleaned_data['ll']
            sg=a.cleaned_data['sg']
            
            
            b=reviewmodel(nm=name,cl=cls,tlm=tl,ccam=cca,psm=ps,hfm=hf,itm=it,ctm=ct,cfm=cf,llm=ll,sgm=sg)
            b.save()
            return HttpResponse("Submitted successfully")
        else:
           return HttpResponse("error") 
    return render(request,'review.html',{'n':n,'cl':cl})

def rev(request,id):
    obj=registermodel.objects.get(id=id)
    cls=obj.clss
    a=reviewmodel.objects.filter(cl=cls)
    return render(request,'rev.html',{'a':a})

def re(request,id):
    obj=reviewmodel.objects.get(id=id)
    return render(request,'re.html',{'obj':obj})

def pnotes(request,id):
    obj=registermodel.objects.get(id=id)
    if request.method=='POST':
        a=pnotesform(request.POST,request.FILES)
        if a.is_valid():
            cl=a.cleaned_data['cl']
            sub=a.cleaned_data['sub']
            chno=a.cleaned_data['chno']
            note=a.cleaned_data['note']

            b=pnotesmodel(cla=cl,su=sub,cno=chno,nt=note)
            b.save()
            return HttpResponse("posted successfully")
        else:
           return HttpResponse("error") 
    return render(request,'pnotes.html',{'c':obj})

def note(request,id):
    obj=regmodel.objects.get(id=id)
    cls=obj.cl
    a=pnotesmodel.objects.filter(cla=cls)
    return render(request,'note.html',{'a':a})

