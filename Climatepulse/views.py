from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
import datetime
from contactenquiry.models import contactenquiry
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as authlogin
from blog.models import blogPost
from contributers.models import contributersDetails
from django.contrib import messages
from quiz.models import quesModel
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import postfrom


# c1 = {
#     'posts': blogPost.objects.all()
# }


def homepage(req):
    c = reversed(blogPost.objects.all())
    if 'city' in req.POST:
        city = req.POST['city']
        if city == '':
            city = 'Delhi'
    else:
        city = 'Delhi'

    appid = '43772fd8a082a9e87d9aedaeb45ce998'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    Params = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=Params)
    res = r.json()
    desc = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    windspeed = res['wind']['speed']
    country = res['sys']['country']
    c_time = datetime.datetime.now()
    city = res['name']

    return render(req, 'index.html', {'desc': desc, 'icon': icon, 'temp': temp, 'city': city, 'wspeed': windspeed, 'time': c_time, 'country': country, 'c': c})


def aboutuspage(req):
    contributersData = {
        'cdata': contributersDetails.objects.all()
    }

    return render(req, 'aboutus.html', contributersData)


# def blogpage(req):

#     return render(req, 'blog.html', c)


class PostView(ListView):
    model = blogPost
    template_name = './templates/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def quizpage(request):
    question = quesModel.objects.all()
    # for q in question:
    #     print(q.ques)
    #     print(q.ans)
    # if request.method =="POST":
    #     a1 = request.POST.get('op1')
    #     a2 = request.POST.get('op2')
    #     print(a1)
    #     print(a2)

    if request.method == 'POST':
        # print(request.POST)
        questions = quesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.ques))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.ques):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quizzresult.html', context)
    else:
        questions = quesModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'quiz.html', context)

    return render(request, 'quiz.html', {'question': question})


def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        en = contactenquiry(contact_name=name,
                            contact_email=email, contact_desc=desc)
        if (name != '' and email != '' and desc != ''):
            en.save()
    return render(request, 'aboutus.html')


def login(request):
    if request.method == "POST":
        login_email = request.POST.get('email')
        login_pass = request.POST.get('password')
        # print(login_email,login_pass)
        user = authenticate(
            request, username=login_email, password=login_pass)
        if user is not None:
            authlogin(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('user or password incorrect')
    return render(request, 'Login.html')


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if name != '' and email != '' and password != '':
            if password != cpassword:
                return HttpResponse('your password not matched')
            else:
                my_user = User.objects.create_user(name, email, password)
                my_user.save()
                return HttpResponseRedirect('/login/')
    return render(request, 'Signup.html')


def logOutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')


def profielPage(req):
    return render(req, 'profile.html')


def blogSearch(request):
    if request.method == "POST":
        svalue = request.POST.get('s_value')
        searchresult = blogPost.objects.filter(title__icontains=svalue)
        # for n in searchresult:
        #     print(n.title)

    return render(request, 'blogSearch.html', {'svalue': searchresult})


def userBlog(request):
    cu = request.user.username
    if cu == '':
        messages.info(request, 'Please login first')
        return HttpResponseRedirect('/login/')
    else:
        blogresult = reversed(blogPost.objects.filter(author_name__username=cu))
    # print(currentuser)
    # for r in blogresult:
    #     print(r.title)
    return render(request, 'userblog.html', {'blogresult': blogresult})


class PostDetailview(DetailView):
    model = blogPost
    template_name = './templates/post_detail.html'


class PostCreateView( CreateView):
    model = blogPost
    form_class =postfrom
    # fields = [  'title', 'content']
    template_name = './templates/addpost.html'

    def form_valid(self, form):
        form.instance.author_name= self.request.user
        return super().form_valid(form)
    


class PostUpdateView( UpdateView):
    model = blogPost
    form_class =postfrom
    # fields = [  'title', 'content']
    template_name = './templates/update_post.html'

    # def form_valid(self, form):
    #     form.instance.author_name= self.request.user
    #     return super().form_valid(form)