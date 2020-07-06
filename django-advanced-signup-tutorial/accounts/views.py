from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import SignUpForm,LoginForm
from .tokens import account_activation_token
from .models import Profile
import pyrebase

def home_view(request):
    return render(request, 'home.html')


def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')

def jigar_checks_database(request):
    print("Database updating")
    config = {
        'apiKey': "AIzaSyDsPRLKwnfbmpkGBlCHz3oDUtClin70aeM",
        'authDomain': "remindersystem-36ffc.firebaseapp.com",
        'databaseURL': "https://remindersystem-36ffc.firebaseio.com",
        'projectId': "remindersystem-36ffc",
        'storageBucket': "remindersystem-36ffc.appspot.com",
        'messagingSenderId': "131939032129",
        'appId': "1:131939032129:web:9813b0c49793331083fac0",
        'measurementId': "G-5DM5CPTD4P",
        'serviceAccount':"accounts\\key.json"
    }
    firebase = pyrebase.initialize_app(config)
    firebase.database()
    db = firebase.database()
    db.child("users").child("person 01")

    data = {
        "name": "Ansh Anchal Jigar ",
        "mobile":"9579088663",
        "gst_no" :"123456789"
    }
    db.push(data)
    print("Database updated")
    return HttpResponse("Hello")
            

def signup_view(request):
    
    if request.method == 'POST':
        login_data = request.POST.dict()
        # print(login_data)
        # print(request.POST)
        # print("Inside Request post")
        form = SignUpForm(request.POST)
        print(request.POST.get('firstname'))
        # form = Profile(request.POST)
        if True:
            print(form)
            print("Form is ready error free")
            # print("Entering signup")
            # user = form.save()
            ##########################3
            #see once
            # user.refresh_from_db()
            # user.profile.firstname = form.cleaned_data.get('firstname')
            # user.profile.lastname = form.cleaned_data.get('lastname')
            # user.profile.username = form.cleaned_data.get('username')
            # user.profile.phone = form.cleaned_data.get('phone')
            # user.profile.email = form.cleaned_data.get('email')
            # print("**==**"*50)

            # user.profile.gst = form.cleaned_data.get('gst')
            # user.profile.aadhar =form.cleaned_data.get('aadhar')
            # user.profile.pan = form.cleaned_data.get("pan")
            # user.profile.password= form.cleaned_data.get("password")
            # user.profile.repass = form.cleaned_data.get("repass")


            
            config = {
            'apiKey': "AIzaSyDsPRLKwnfbmpkGBlCHz3oDUtClin70aeM",
            'authDomain': "remindersystem-36ffc.firebaseapp.com",
            'databaseURL': "https://remindersystem-36ffc.firebaseio.com",
            'projectId': "remindersystem-36ffc",
            'storageBucket': "remindersystem-36ffc.appspot.com",
            'messagingSenderId': "131939032129",
            'appId': "1:131939032129:web:9813b0c49793331083fac0",
            'measurementId': "G-5DM5CPTD4P",
            "serviceAccount":"accounts\\key.json"
            }
            firebase = pyrebase.initialize_app(config)
            firebase.database()
            auth = firebase.auth()
            users =auth.create_user_with_email_and_password(request.POST.get('email'), request.POST.get('repass'))
            print("**"*50)
            # print(users)
            # user = auth.sign_in_with_email_and_password(user.profile.email, user.profile.password)

            db = firebase.database()
            db.child("users").child("person 01")

            data = {
                "firstname": request.POST.get('firstname'),
                "lastname":request.POST.get('lastname'),
                "username":request.POST.get('username'),
                "phone":request.POST.get('phone'),
                "email":request.POST.get('email'),
                "gst":request.POST.get('gst'),
                "aadhar": request.POST.get('aadhar'),
                "pan":request.POST.get('pan'),
                "pass":request.POST.get('pass'),
                "repass":request.POST.get('repass')
                
                }
            db.push(data)   
            print("Jigar Joshi")
            print("=="*50)
            print("=="*50)
            print("=="*50)
            print("=="*50)
            print("=="*50)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # subject = 'Please Activate Your Account'
            # message = render_to_string('activation_request.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)
            # return redirect('activation_sent')
        else:
            print(form._errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    print("lOGIN IS Working")
    form = LoginForm(request.POST)
    if request.method =="POST":
        print("request is post")
        print(form)
        config = {
            'apiKey': "AIzaSyDsPRLKwnfbmpkGBlCHz3oDUtClin70aeM",
            'authDomain': "remindersystem-36ffc.firebaseapp.com",
            'databaseURL': "https://remindersystem-36ffc.firebaseio.com",
            'projectId': "remindersystem-36ffc",
            'storageBucket': "remindersystem-36ffc.appspot.com",
            'messagingSenderId': "131939032129",
            'appId': "1:131939032129:web:9813b0c49793331083fac0",
            'measurementId': "G-5DM5CPTD4P",
            "serviceAccount":"accounts\\key.json"
        }
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        login_data = request.POST.dict()
        print(login_data)
        print(request.POST)
        print("Inside Request post")
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        users = auth.sign_in_with_email_and_password(request.POST.get('email'), request.POST.get('password'))
    return render(request, 'login.html')
