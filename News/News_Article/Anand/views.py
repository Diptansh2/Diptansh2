from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from Anand.models import RegisterForm, rightpostform, leftpostform, astrologypostform, internationalpostform, lifestylepostform, latestpostform, sportpostform, technicalpostform
from schedule.models import Calendar
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
#from finalResult.models import LoginForm
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import PDFFile
from .forms import PDFFileForm

# def upload_pdf(request):
#     if request.method == 'POST':
#         form = PDFFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('pdf_detail', pk=form.instance.pk)  # Redirect to PDF detail page
#     else:
#         form = PDFFileForm()
#     return render(request, 'post/upload_pdf.html', {'form': form})

# def pdf_detail(request, pk):
#     pdf = get_object_or_404(PDFFile, pk=pk)
#     return render(request, 'dashboard/pdf_detail.html', {'pdf': pdf})

def news(request):
    selected_type = request.GET.get('type', 'latest')  # Default to 'latest' if no type selected
    articles = Article.objects.filter(news_type=selected_type)
    context = {
        'articles': articles,
        'selected_type': selected_type,
    }
    return render(request, 'dashboard/base.html', context)


def news1(request):
    latest_data = latestpostform.objects.all().order_by('-created_at')
    technical_data = technicalpostform.objects.all().order_by('-created_at')
    international_data = internationalpostform.objects.all().order_by('-created_at')
    sport_data = sportpostform.objects.all().order_by('-created_at')
    right_data = rightpostform.objects.all().order_by('created_at')
    left_data = leftpostform.objects.all().order_by('created_at')
    astrology_data=astrologypostform.objects.all().order_by('-created_at')
    lifestyle_data=lifestylepostform.objects.all().order_by('-created_at')
    
    context = {
        'latest_data': latest_data,
        'technical_data': technical_data,
        'international_data': international_data,
        'sport_data': sport_data,
        'right_data': right_data,
        'left_data': left_data,
        'astrology_data': astrology_data,
        'lifestyle_data': lifestyle_data,
    }

    return render(request, 'dashboard/navbar.html', context)
# Define your latest(), sport(), international(), and technical() functions here



def latest(request):
    if request.method == 'POST':
        ulatest_data = request.POST.get('ulatest', '')  # Get the submitted ulatest data
        ualatest_data = request.POST.get('ualatest', '')  # Get the submitted ualatest data
        
        # Create a new instance of the latestpostform model and save it
        data_model = latestpostform.objects.create(
            ulatestpost=ulatest_data,
            ualatestpost=ualatest_data
        )
        
        # Access and print the data_model instance
        print("New data saved - ulatest:", data_model.ulatestpost, "ualatest:", data_model.ualatestpost, "at:", data_model.created_at)
        
        return redirect('latest')  # Redirect to the latest view to display the data

    latest_data = latestpostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/latest.html', {'latest_data': latest_data})#     if request.method == 'POST':
        
def sport(request):
    if request.method == 'POST':
        usport_data = request.POST.get('usport', '')  # Get the submitted usport data
        uasport_data = request.POST.get('uasport', '')  # Get the submitted uasport data
        
        # Create a new instance of the sportpostform model and save it
        data_model = sportpostform.objects.create(
            usportpost=usport_data,
            uasportpost=uasport_data
        )
        
        # Access and print the data_model instance
        print("New data saved - usport:", data_model.usportpost, "uasport:", data_model.uasportpost, "at:", data_model.created_at)
        
        return redirect('sport')  # Redirect to the sport view to display the data

    sport_data = sportpostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/article_list.html', {'sport_data': sport_data})#     if request.method == 'POST':
# 
def international(request):
    if request.method == 'POST':
        uinternational_data = request.POST.get('uinternational', '')  # Get the submitted uinternational data
        uainternational_data = request.POST.get('uainternational', '')  # Get the submitted uainternational data
        
        # Create a new instance of the internationalpostform model and save it
        data_model = internationalpostform.objects.create(
            uinternationalpost=uinternational_data,
            uainternationalpost=uainternational_data
        )
        
        # Access and print the data_model instance
        print("New data saved - uinternational:", data_model.uinternationalpost, "uainternational:", data_model.uainternationalpost, "at:", data_model.created_at)
        
        return redirect('international')  # Redirect to the international view to display the data

    international_data = internationalpostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/new.html', {'international_data': international_data})#     if request.method == 'POST':


def technical(request):
    if request.method == 'POST':
        utechnical_data = request.POST.get('utechnical', '')  # Get the submitted utechnical data
        uatechnical_data = request.POST.get('uatechnical', '')  # Get the submitted uatechnical data
        
        # Create a new instance of the technicalpostform model and save it
        data_model = technicalpostform.objects.create(
            utechnicalpost=utechnical_data,
            uatechnicalpost=uatechnical_data
        )
        
        # Access and print the data_model instance
        print("New data saved - utechnical:", data_model.utechnicalpost, "uatechnical:", data_model.uatechnicalpost, "at:", data_model.created_at)
        
        return redirect('technical')  # Redirect to the technical view to display the data

    technical_data = technicalpostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/tech.html', {'technical_data': technical_data})#     if request.method == 'POST':


def astrology(request):
    if request.method == 'POST':
        uastrology_data = request.POST.get('uastrology', '')  # Get the submitted uastrology data
        uaastrology_data = request.POST.get('uaastrology', '')  # Get the submitted uaastrology data
        
        # Create a new instance of the astrologypostform model and save it
        data_model = astrologypostform.objects.create(
            uastrologypost=uastrology_data,
            uaastrologypost=uaastrology_data
        )
        
        # Access and print the data_model instance
        print("New data saved - uastrology:", data_model.uastrologypost, "uaastrology:", data_model.uaastrologypost, "at:", data_model.created_at)
        
        return redirect('astrology')  # Redirect to the astrology view to display the data

    astrology_data = astrologypostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/astrology.html', {'astrology_data': astrology_data})#     if request.method == 'POST':

def lifestyle(request):
    if request.method == 'POST':
        ulifestyle_data = request.POST.get('ulifestyle', '')  # Get the submitted ulifestyle data
        ualifestyle_data = request.POST.get('ualifestyle', '')  # Get the submitted ualifestyle data
        
        # Create a new instance of the lifestylepostform model and save it
        data_model = lifestylepostform.objects.create(
            ulifestylepost=ulifestyle_data,
            ualifestylepost=ualifestyle_data
        )
        
        # Access and print the data_model instance
        print("New data saved - ulifestyle:", data_model.ulifestylepost, "ualifestyle:", data_model.ualifestylepost, "at:", data_model.created_at)
        
        return redirect('lifestyle')  # Redirect to the lifestyle view to display the data

    lifestyle_data = lifestylepostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/lifestyle.html', {'lifestyle_data': lifestyle_data})#     if request.method == 'POST':



def right(request):
    if request.method == 'POST':
        uright_data = request.POST.get('uright', '')  # Get the submitted uright data
        uaright_data = request.POST.get('uaright', '')  # Get the submitted uaright data
        
        # Create a new instance of the rightpostform model and save it
        data_model = rightpostform.objects.create(
            urightpost=uright_data,
            uarightpost=uaright_data
        )
        
        # Access and print the data_model instance
        print("New data saved - uright:", data_model.urightpost, "uaright:", data_model.uarightpost, "at:", data_model.created_at)
        
        return redirect('right')  # Redirect to the right view to display the data

    right_data = rightpostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/right.html', {'right_data': right_data})#     if request.method == 'POST':

def left(request):
    if request.method == 'POST':
        uleft_data = request.POST.get('uleft', '')  # Get the submitted uleft data
        ualeft_data = request.POST.get('ualeft', '')  # Get the submitted ualeft data
        
        # Create a new instance of the leftpostform model and save it
        data_model = leftpostform.objects.create(
            uleftpost=uleft_data,
            ualeftpost=ualeft_data
        )
        
        # Access and print the data_model instance
        print("New data saved - uleft:", data_model.uleftpost, "ualeft:", data_model.ualeftpost, "at:", data_model.created_at)
        
        return redirect('left')  # Redirect to the left view to display the data

    left_data = leftpostform.objects.all().order_by('-created_at')
    return render(request, 'dashboard/left.html', {'left_data': left_data})#     if request.method == 'POST':



def latestpost(request):
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        ulatest_data = request.POST.get("ulatest")
        ualatest_data = request.POST.get("ualatest")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
       

        data = latestpostform(ulatestpost=ulatest_data, ualatestpost=ualatest_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
        
    
    latest_data = latestpostform.objects.all()  # Query all data from the model
    return render(request, 'post/latestpost.html', {'latest_data': latest_data})


def internationalpost(request):
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        uinternational_data = request.POST.get("uinternational")
        uainternational_data = request.POST.get("uainternational")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        data = internationalpostform(uinternationalpost=uinternational_data, uainternationalpost=uainternational_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
    
    international_data = internationalpostform.objects.all()  # Query all data from the model
    return render(request, 'post/newpost.html', {'international_data': international_data})

    
def technicalpost(request):
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        utechnical_data = request.POST.get("utechnical")
        uatechnical_data = request.POST.get("uatechnical")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        data = technicalpostform(utechnicalpost=utechnical_data, uatechnicalpost=uatechnical_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
    
    technical_data = technicalpostform.objects.all()  # Query all data from the model
    return render(request, 'post/techpost.html', {'technical_data': technical_data})


def sportpost(request):
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        usport_data = request.POST.get("usport")
        uasport_data = request.POST.get("uasport")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        data = sportpostform(usportpost=usport_data, uasportpost=uasport_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
    
    sport_data = sportpostform.objects.all()  # Query all data from the model
    return render(request, 'post/updatedpost.html', {'sport_data': sport_data})


def astrologypost(request):
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        uastrology_data = request.POST.get("uastrology")
        uaastrology_data = request.POST.get("uaastrology")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
       

        data = astrologypostform(uastrologypost=uastrology_data, uaastrologypost=uaastrology_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
        
    
    astrology_data = astrologypostform.objects.all()  # Query all data from the model
    return render(request, 'post/astrologypost.html', {'astrology_data': astrology_data})


def lifestylepost(request):
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        ulifestyle_data = request.POST.get("ulifestyle")
        ualifestyle_data = request.POST.get("ualifestyle")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
       

        data = lifestylepostform(ulifestylepost=ulifestyle_data, ualifestylepost=ualifestyle_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
        
    
    lifestyle_data = lifestylepostform.objects.all()  # Query all data from the model
    return render(request, 'post/lifestylepost.html', {'lifestyle_data': lifestyle_data})




def rightpost(request):
    
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")
    
    if request.method == 'POST' and request.FILES['upload']:
        uright_data = request.POST.get("uright")
        uaright_data = request.POST.get("uaright")
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        data = rightpostform(urightpost=uright_data, uarightpost=uaright_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")
    
    right_data = rightpostform.objects.all()  # Query all data from the model
    return render(request, 'post/rightadd.html', {'right_data': right_data})


# def leftpost(request):
#      if request.method == 'POST' and request.FILES['upload']:
#         uleft_data = request.POST.get("uleft")
#         ualeft_data = request.POST.get("ualeft")
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         data = leftpostform(uleftpost=uleft_data, ualeftpost=ualeft_data, img_url=file_url)
#         data.save()
#         print("Data Saved Successfully")
    
#      left_data = leftpostform.objects.all()  # Query all data from the model
#      return render(request, 'post/leftadd.html', {'left_data': left_data})


def leftpost(request):
    # Check if the user has a valid session with 'email' and 'ps' variables set
    if not request.session.get('email') or request.session.get('ps') != True:
        return HttpResponse("Get out! You are not authorized")

    if request.method == 'POST' and request.FILES.get('upload'):
        # Retrieve form data and uploaded file
        uleft_data = request.POST.get("uleft")
        ualeft_data = request.POST.get("ualeft")
        upload = request.FILES['upload']

        # Save the uploaded file
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)

        # Create a new instance of the 'leftpostform' model and save it
        data = leftpostform(uleftpost=uleft_data, ualeftpost=ualeft_data, img_url=file_url)
        data.save()
        print("Data Saved Successfully")

    # Query all data from the 'leftpostform' model
    left_data = leftpostform.objects.all()

    # Render the 'post/leftadd.html' template and pass the 'left_data' to it
    return render(request, 'post/leftadd.html', {'left_data': left_data})

def registerview(request):
    if request.method=='POST':
        nam1=request.POST["na"]
        em1=request.POST['em']
        pa1=request.POST['pw']
        cus=request.POST['course']
        
        gen=request.POST['gender']
        print(nam1,em1,pa1,cus,gen)
        data=RegisterForm(uname=nam1,uemail=em1,upass=pa1,ucourse=cus,ugender=gen)
        data.save()
        print("Data Saved Successfuly")    
    return render(request, 'entry/registration.html')

def loginview(request):
    if request.method=='POST':
        '''
        em1=request.POST['em']
        pa1=request.POST['pw']
        print (em1,pa1)
        
        auth_data=RegisterForm.objects.filter(uemail=em1).values('upass')
        
        for data in auth_data:
            global pa2
            pa2=data['upass']
        print("Your current password=",pa2)
        if pa1==pa2:
            print("Login Successful")
            return render(request, 'finalpage/dashboard.html')
        else:
            print("Login Failed!! Check Your Password")
            '''
        emp=RegisterForm.objects.get(uemail=request.POST['em'])
        print(emp.upass)
        if emp.upass==request.POST['pw']:
            request.session["email"]=emp.uemail
            request.session["ps"]=True
            #return HttpResponse("Conrats You are logged in")
            print("Login succesful and session stored")
            print("session=",request.session["email"],request.session["ps"],request.session)
            return render(request, 'entry/dash.html')
        else:
            return HttpResponse("so sad please check your credentials")
    return render(request, 'entry/login.html')

def dashboardview(request):
    if request.session.get('email'):
        if request.session.get('ps')==True:
            return render(request,'entry/dash.html')
    else:
        return HttpResponse("Get out! You are not authorised")


def logout(request):
    try:
        del request.session["email"]
        del request.session["ps"]
    except KeyError:
        pass
    return HttpResponse("You are logged out")



def calendar_view(request):
    calendar = Calendar.objects.get_or_create(name='My Calendar')[0]
    return render(request, 'dashboard/calendar.html', {'calendar': calendar})

