from django import forms 
  
  
class Form(forms.Form): 
    url_nm = forms.URLField( )