from django.shortcuts import render, get_object_or_404, redirect
from .models import Bar, Blog
from .forms import BlogPost
from django.utils import timezone
from django.core.paginator import Paginator
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def bar(request):
    bars = Bar.objects
    bars_list=Bar.objects.all()
    paginator = Paginator(bars_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'bar.html', {'bars':bars,'posts':posts})

def bard(request, bar_id):
    bard = get_object_or_404(Bar, pk = bar_id)
    return render(request, 'bard.html', {'bar':bard})

def blog(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'blog.html',{'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('blog')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})

def cock(request):
        url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a"
        data = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a").json()

        drinkdata = data["drinks"]
        
        cocks = {}
        i = 0
        for cocktail in drinkdata:
                cocks[i] = [cocktail["strDrink"], cocktail["strAlcoholic"], cocktail["strDrinkThumb"]]
                i+=1

        '''for cocktail in drinkdata:
                cocks = {
                "name" : cocktail["strDrink"],
                "alc" : cocktail["strAlcoholic"],
                "img" : cocktail["strDrinkThumb"]
                }
        '''
        return render(request, 'cock.html', {'cocks':cocks})