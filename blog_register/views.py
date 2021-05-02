from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import Blog

# Create your views here.
def blog_list(request):
    return render(request,"blog_register/blog_list.html",{'blog_list':Blog.objects.all()})

def blog_form(request,id=0):
    if request.method =="GET":
        if id==0:
            form = BlogForm()
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogForm(instance =blog)
        return render(request,"blog_register/blog_form.html",{'form':form})
    else:
        if id==0:
            form = BlogForm(request.POST, request.FILES)
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogForm(request.POST,instance =blog)
        if form.is_valid():
            form.save()
        return redirect('/blog/list')

def blog_delete(request,id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('/blog/list/')