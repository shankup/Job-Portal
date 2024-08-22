from django.shortcuts import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date



# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin_login.html')


# Recruiter signup

def recruiter_signup(request):
    fm=''
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        p=request.POST['pwd']
        e=request.POST['email']
        company=request.POST['company']
        con=request.POST['contact']
        gen=request.POST['gender']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Recruiter.objects.create(user=user,mobile=con,gender=gen,type="recruiter",company=company,status="pending")
            fm="no"
        except:
            fm="yes"
    d={'fm':fm}
    
    return render(request,'recruiter_signup.html',d)

# Recruiter Login
def recruiter_login(request):
    fm=""
    if request.method=="POST":
        u=request.POST["uname"];
        p=request.POST["pwd"];
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1=Recruiter.objects.get(user=user)
                if user1.type=="recruiter":
                    login(request,user) #login it is a inbuilt function by Django
                    return redirect('recruiter_home')
                else:
                    fm="yes"
            except:
                fm="yes"
        else:
            fm="yes"
    d={"fm":fm}
    return render(request,'recruiter_login.html',d)


# Recruiter profile page


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    recruiter_profile = Recruiter.objects.get(user=request.user)
    d = {'recruiter_profile': recruiter_profile}
    return render(request, 'recruiter_home.html', d)

# user Signup
def user_signup(request):
    fm=''
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        p=request.POST['pwd']
        e=request.POST['email']
        con=request.POST['contact']
        gen=request.POST['gender']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            StudentUser.objects.create(user=user,mobile=con,gender=gen,type="student")
            fm="no"
        except:
            fm="yes"
    d={'fm':fm}
    return render(request,'user_signup.html',d)

# user login

def user_login(request):
    fm=""
    if request.method=="POST":
        u=request.POST["uname"];
        p=request.POST["pwd"];
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1=StudentUser.objects.get(user=user)
                if user1.type=="student":
                    login(request,user) #login it is a inbuilt function by Django
                    fm="no"
                else:
                    fm="yes"
            except:
                fm="yes"
        else:
            fm="yes"
    d={"fm":fm}
    return render(request,'user_login.html',d)


# User profile page

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user_profile = StudentUser.objects.get(user=request.user)
    return render(request, 'user_home.html', {'user_profile': user_profile})


#user logout

def Logout(request):
    logout(request)   # logout it is a inbuilt function by Django
    return redirect('index')


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    fm=''
    if request.method=='POST':
        jt=request.POST['jobtitle']
        sd=request.POST['startdate']
        ed=request.POST['enddate']
        sal=request.POST['salary']
        loc=request.POST['location']
        exp=request.POST['experience']
        l=request.FILES['logo']
        skills=request.POST['skills']
        des=request.POST['description']
        user=request.user
        recruiter=Recruiter.objects.get(user=user) # beacause we use recruiter as forginkey in models(Job)
        try:
            Job.objects.create(recruiter=recruiter,start_date=sd,end_date=ed,title=jt,salary=sal,image=l,description=des,experience=exp,location=loc,skills=skills,creationdate=date.today()) # recruiter=request.user it is uue for current user
            fm="no"
        except:
            fm="yes"
    d={'fm':fm}
    return render(request,'add_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user=request.user
    recruiter=Recruiter.objects.get(user=user)# it is use for getting recruiter from current user
    job=Job.objects.filter(recruiter=recruiter) #it is use for getting data from current Recruiter
    d={'job':job}
    return render(request,'job_list.html',d)

def delete_job(request, job_id):
    # Assuming Job is your model name
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('job_list')


# For letest job an home page

def letest_jobs(request):
    job=Job.objects.all().order_by('start_date')
    d={'job':job}
    return render(request,'latest_jobs.html',d)

def user_letestjob(request):
    job=Job.objects.all().order_by('start_date')
    user=request.user # current user select
    student=StudentUser.objects.get(user=user) # fetch data from current student studentuser
    data=Apply.objects.filter(student=student) #how many times apply job by user its fatch all and filter
    li=[]
    for i in data:
        li.append(i.job.id) # job_id from job field in Apply models
    d={'job':job,'li':li}
    return render(request,'user_latestjob.html',d)

def job_detail(request,pid):
    job=Job.objects.get(id=pid)
    d={'job':job}
    return render(request,'job_detail.html',d)

def applyforjob(request, pid):
    if not request.user.is_authenticated:
        return redirect("user_login")
    fm = ""
    user=request.user
    student = StudentUser.objects.get(user=user)
    job=Job.objects.get(id=pid)
    date1=date.today()
    if job.end_date<date1:
        fm="close"
    elif job.start_date>date1:
        fm="notopen"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(job=job,student=student,resume=r,applydate=date.today())
            fm="done"
            
    
    d = {'fm': fm}
    return render(request, 'applyforjob.html', d)


# applied candidate list in recricter
def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    data=Apply.objects.all()
    d = {'data': data}
    return render(request, 'applied_candidatelist.html', d)

