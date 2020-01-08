from __future__ import unicode_literals ,print_function

from django.shortcuts import *

from .models import *
import smtplib
from django.http import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import *
from django.contrib import messages
from django.db.models import Q

def index(request):
    post = Post.objects.all()
    context = { 'post': post , 'image':post}
    return render(request, 'src/blog/blog_page.html' , context)
    
def login_panal(request):
    return render(request,'login.html')
def dashbord(request):
    return render(request,'src/index.html')
def product(request):
    return render(request,'src/porduct.html')
def blog_admin(request):

    return render(request,'src/blog/blog_admin.html')
def see_post(request):
    post = Post.objects.all()
    context = { 'post': post}
    return render(request, 'src/blog/see_blog_post.html' ,context)

##def blog_post(request):
##    post = Post.objects.all()
##    context = { 'post': post , 'image':post}
##    return render(request, 'src/blog/blog_page.html' , context)

def hello(request):
    books = Booklist.objects.all()
    context = {
        'books': books
    }
    return render(request,'src/curd/show_book_1.html' , context)

def penlist(request):
    pen = Penlist.objects.all()
    context = {
       'pen' : pen
    }

    return render(request,'src/curd/show_pen_1.html' , context)






def login(request):
   context ={}
   if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('blog_admin'))
    else:
        return render(request, 'login.html',{'error':'User name or password not matching'})
   else:
    return  render(request, 'login.html',context)
def user_logout(request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))





def book_create_1(request):
    print(request.POST)
    title = request.POST.get('title')
    price = request.POST.get('price')
    author = request.POST.get('author')
    book_details = Booklist(title=title, price=price, author=author)
    book_details.save()
    return redirect('hello')

def create_post(request):
    print(request.POST)
    post = request.POST.get('post')
    image = request.FILES['image']
    post_details = Post(post=post ,image=image)
    post_details.save()
    return redirect('blog_admin')

def pen_create_1(request):
    print(request.POST)
    title  = request.POST.get('title')
    price =  request.POST.get('price')
    Customer = request.POST.get('Customer')
    pen_details = Penlist(title=title, price=price, Customer=Customer)
    pen_details.save()
    return redirect('pen')


def add_book_1(request):

    return render(request, 'src/curd/add_book.html')
def add_pen_1(request):
    return render(request, 'src/curd/add_pen_1.html')



def delete_book_1(request, id):
    books = Booklist.objects.get(pk=id)
    books.delete()
    return redirect('hello')

def delete_pen_1(request,id):
    pen = Penlist.objects.get(pk=id)
    pen.delete()
    return redirect('pen')
def delete_blog(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('see_post')

def edit_book_1(request, id):
    books = Booklist.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'src/curd/edit_book_1.html', context)

def edit_pen_1(request, id):
    pen = Penlist.objects.get(pk=id)
    context = {
          'pen':pen
    }
    return render(request,'src/curd/edit_pen_1.html' ,context)

def edit_blog(request, id):
    post = Post.objects.get(pk=id)
    context = {'post':post}
    return render(request, 'src/blog/edit_blog.html', context)


def update_book_1(request, id):
    books = Booklist.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('hello')
def update_blog(request, id):
    post = Post.objects.get(pk=id)
    post.post  = request.POST.get('post')
    post.image = request.FILES['image']
    post.save()
    return redirect('see_post')

def update_pen_1(request, id):
    pen = Penlist.objects.get(pk=id)
    pen.title  = request.GET['title']
    pen.price =  request.GET['price']
    pen.Customer = request.GET['Customer']
    pen.save()
    return redirect('pen')
##select use for testing testfild
def select(request):
    print(request.POST)
    option = request.POST.get('option')
    option_change = Select(option=option)
    option_change.save()
    return redirect('blog_post')

def cal(request):
    print(request.POST)
    num1 = request.POST.get('num1')
    num2 = request.POST.get('num2')

##---------------------Outside Code---------------------------
def sending_main(request):
    print (request.POST)
    Subject = request.POST.get('subject')
    mail = request.POST.get('mail')
    send_to = request.POST.get('sender')
    user = 'rjkabir23@gmail.com'
    password = '0123456789rafan'
    send_adress = send_to
    subject =  raw_input(Subject)
    msg = raw_input(mail)


    try:
       server = smtplib.SMTP('smtp.gmail.com:587')
       server.ehlo()
       server.starttls()
       server.login(user,password)
       massage = 'Subject {0} \n \n {1}'.format(subject,msg)
       server.sendmail(user,send_adress,massage)
       server.quit()
       print ('Massages Sending Success fully Complete')
       context = {'error':'Success'}
    except smtplib.SMTPException as msg:
      print ('Some Thing Wrong \n\n')
      print (msg)
      context = {'error':msg}
    return render(request, 'src/blog/blog_page.html' , context)








# Create your views here.
