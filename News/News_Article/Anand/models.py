from django.db import models
from django.utils import timezone

class Article(models.Model):
    # other fields
    NEWS_TYPES = [
        ('latest', 'Latest Article'),
        ('sport', 'Updated Article'),
        ('international', 'New Article'),
        ('tech','Technical Article'),
        # add more types if needed
    ]
    news_type = models.CharField(max_length=20, choices=NEWS_TYPES, default='latest')
    # other fields and methods

class RegisterForm(models.Model):
    GENDER_CHOICE=(('male','MALE'),('female','FEmale'))
    COURSE_CHOICE=(('java','JAVA'),('python','PYTHON'))
    uname= models.CharField(max_length=50)
    uemail=models.CharField(max_length=35)
    upass=models.CharField(max_length=12)
    ugender=models.CharField(max_length=8,choices=GENDER_CHOICE,default='male')
    ucourse=models.CharField(max_length=50,choices=COURSE_CHOICE,default='Aadhar Card')
    

class latestpostform(models.Model):
     ulatestpost= models.TextField(default='')
     ualatestpost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')
# class latestpostform(models.Model):
#     ulatestpost= models.CharField(default='')
#     content = models.TextField(default="Default content goes here.")

    # def __str__(self):
    #     return self.title
    
class sportpostform(models.Model):
     usportpost= models.TextField(default='')
     uasportpost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')
    
class internationalpostform(models.Model):
     uinternationalpost= models.TextField(default='')
     uainternationalpost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')
    
class technicalpostform(models.Model):
     utechnicalpost= models.TextField(default='')
     uatechnicalpost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')
     
class leftpostform(models.Model):
     uleftpost= models.TextField(default='')
     ualeftpost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')
     
class rightpostform(models.Model):
     urightpost= models.TextField(default='')
     uarightpost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')
  
class astrologypostform(models.Model):
     uastrologypost= models.TextField(default='')
     uaastrologypost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')   

class lifestylepostform(models.Model):
     ulifestylepost= models.TextField(default='')
     ualifestylepost= models.TextField(default='')
     created_at = models.DateTimeField(default=timezone.now)
     img_url=models.ImageField(upload_to='images/', default='')   

class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title