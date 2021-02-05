from django.shortcuts import render 
from .forms import Form 
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
from django.http import JsonResponse
from nltk.corpus import stopwords
from .models import url
import json

  

def home_view(request): 
    context = {} 
    context['form'] = Form()
    return render( request, "home.html", context)
        
def result_view(request):
    if request.POST: 
        temp = request.POST['url_nm']
        source_code = requests.get(temp).text
        soup = BeautifulSoup(source_code, 'html.parser')
        wordlist=[]
        content =soup.get_text()
        words = content.lower().split()
        en_stops = set(stopwords.words('english'))
        for word in words: 
            if word not in en_stops:
                wordlist.append(word)

        clean_list =[] 
        for word in wordlist: 
            symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/.,~–` '
            
            for i in range (0, len(symbols)): 
                word = word.replace(symbols[i], '') 
                
            if len(word) > 0: 
                clean_list.append(word)  
        c=Counter(clean_list)
        top = c.most_common(10)
        top=dict(top)
        if not url.objects.filter(url_nm=temp).exists():
            url.objects.create(url_nm=temp,res=json.dumps(top))
            context = {'url_name': top,'msg':"freshly processed data"}
            return render(request, 'result.html', context)
        else :
            result=url.objects.get(url_nm=temp)
            result=json.loads(result.res)
            context = {'url_name': result,'msg':"data from database"}
            return render(request, 'result.html', context)