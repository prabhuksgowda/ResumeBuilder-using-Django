
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,User
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')
# def index1(request):
#     return render(request, 'index1.html')

def index(request):
    if request.user.is_authenticated:
        details = Details.objects.filter(user=request.user).all()
        education = Education.objects.filter(user=request.user).all()
        project = Project.objects.filter(user=request.user).all()
        personaldetails = Personaldetails.objects.filter(user=request.user).all()
        return render(request, 'index.html', {'edu': education, 'pro': details, 'proj': project, 'pd': personaldetails})
    return render(request, 'index.html',)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
    form = UserCreationForm
    return render(request, 'register.html', {'form': form})

def SignIn(request):
    form = SignInForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login.html', {'form': form, 'msg': '* Username or Password Incorrect'})
        else:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login')
def details(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        linkedin = request.POST['linkedin']
        carrearobject = request.POST['carrearobject']
        pro = Details(name=name, email=email, mobile=mobile, linkedin=linkedin, carrearobject=carrearobject, user=request.user)
        pro.save()
        return redirect('index')
    form = DetailsForm()
    return render(request, 'details.html', {'form': form})

def edit_details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST,instance=request.user.details)
        if form.is_valid:
            form.save()
            print('Form valid success')
            return redirect('index')
    form = DetailsForm(instance=request.user.details)
    return render(request, 'details.html', {'form': form})

@login_required(login_url='/login')
def education(request):
    if request.method == 'POST':
        collagename = request.POST['collagename']
        university = request.POST['university']
        branch = request.POST['branch']
        yearofpass = request.POST['yearofpass']
        programinglang = request.POST['programinglang']
        frontendlng = request.POST['frontendlng']
        framework = request.POST['framework']
        cgpa = request.POST['cgpa']
        edu = Education( collagename=collagename,  university=university, branch=branch, yearofpass=yearofpass, programinglang=programinglang, frontendlng=frontendlng, framework=framework, cgpa=cgpa, user=request.user)
        edu.save()
        return redirect('index')
    form = EducationForm()
    return render(request, 'education.html', {'form': form} )

def edit_education(request, pk):
    edu = Education.objects.get(id=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=edu)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EducationForm(instance=edu)
    return render(request, 'education.html', {'form': form})

@login_required(login_url='/login')
def project(request):
    if request.method == 'POST':
        projecttitle = request.POST['projecttitle']
        prodescrip = request.POST['prodescrip']
        proj = Project(projecttitle=projecttitle, prodescrip=prodescrip,user=request.user)
        proj.save()
        return redirect('index')
    form = ProjectForm()
    return render(request, 'project.html', {'form': form})

def edit_project(request, pk):
    proj = Project.objects.get(id=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ProjectForm(instance=proj)
    return render(request, 'project.html', {'form': form})

@login_required(login_url='/login')
def personaldetails(request):
    if request.method == 'POST':
        dob = request.POST['dob']
        gender = request.POST['gender']
        nationality = request.POST['nationality']
        fathername = request.POST['fathername']
        address = request.POST['address']
        strength = request.POST['strength']
        hobbies = request.POST['hobbies']
        pd = Personaldetails(strength=strength,hobbies=hobbies, nationality=nationality, address=address, fathername=fathername, dob=dob, gender=gender, user=request.user)
        pd.save()
        return redirect('index')
    form = PersonaldetailsForm()
    return render(request, 'personaldetails.html', {'form': form})

def edit_personaldetails(request, pk):
    pd = Personaldetails.objects.get(id=pk)
    if request.method == 'POST':
        form = PersonaldetailsForm(request.POST, instance=pd)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PersonaldetailsForm(instance=pd)
    return render(request, 'personaldetails.html', {'form': form})




@login_required(login_url='/login')
def resume(request):
    context = {
         'pro': Details.objects.filter(user=request.user).all(),
         'edu': Education.objects.filter(user=request.user).all(),
         'proj': Project.objects.filter(user=request.user).all(),
         'pd': Personaldetails.objects.filter(user=request.user).all(),
    }
    return render(request, 'Resume.html', context)