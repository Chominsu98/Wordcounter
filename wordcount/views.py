from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")   

def result(request):
    text=request.GET["fulltext"]
    var_for_count=list(text)
    sum=0
    length=len(var_for_count)
    for i in var_for_count:
        if i!=" " and i!="\n":
            sum+=1
    words=text.split()
    word_dictionary={}
    
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    return render(request,"result.html",{'sum':sum,'length':length,'full':text,"total":len(words),"dictionary":word_dictionary.items()})       