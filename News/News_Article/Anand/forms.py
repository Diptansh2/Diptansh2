from django import forms
from .models import latestpostform, astrologypostform, technicalpostform, lifestylepostform, sportpostform, internationalpostform, PDFFile
# from .models import PDFFile
# class latestform(forms.ModelForm):
#     class Meta:
#         model = latestpostform
#         fields = ['ulatestpost', 'content']
#         fields = ['ualatestpost', 'content']
        
# class sportform(forms.ModelForm):
#     class Meta:
#         model = sportpostform
#         fields = ['usportpost', 'content']
#         fields = ['uasportpost', 'content']
        
# class technicalform(forms.ModelForm):
#     class Meta:
#         model = technicalpostform
#         fields = ['utechnicalpost', 'content']
#         fields = ['uatechnicalpost', 'content']
        
# class internationalform(forms.ModelForm):
#     class Meta:
#         model = internationalpostform
#         fields = ['uinternationalpost', 'content']
#         fields = ['uainternationalpost', 'content']
        
# class astrologyform(forms.ModelForm):
#     class Meta:
#         model = astrologypostform
#         fields = ['uastrologypost', 'content']
#         fields = ['uaastrologypost', 'content']
        
# class lifestyleform(forms.ModelForm):
#     class Meta:
#         model = lifestylepostform
#         fields = ['ulifestylepost', 'content']
#         fields = ['ualifestylepost', 'content']
        


class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['title', 'pdf_file']