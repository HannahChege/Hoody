from django.http  import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render
from .forms import SignupForm,NewHoodForm,ProfileForm,BusinessForm,CreatePostForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood,Business,Profile,Post,Join

# Create your views here.
@login_required(login_url='/accounts/login/')
def hood(request):
    """
    Renders the index page
    """
    if Join.objects.filter(user_id = request.user).exists():
        neighbourhood = NeighbourHood.objects.get(pk = request.user.join.hood_id)
        # occupants = Profile.get_user_by_hood(id= request.user.join.hood_id).all()
        posts = Post.get_post_by_hood(id = request.user.join.hood_id)
        # bussiness = Business.objects.get(id = request.user.join.hood_id)
        return render(request,'hood.html', locals())

    else:
        hoods = NeighbourHood.objects.all()
        return render(request, 'index.html', locals())




@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.profile = current_user.profile
            hood.user = current_user

            hood.save()
        return redirect('hood')

    else:
        form = NewHoodForm()
    return render(request, 'new_hood.html', {"form": form})


def search_results(request):

    if 'hood' in request.GET and request.GET["hood"]:
        search_term = request.GET.get("hood")
        searched_hoods = Hood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"hoods": searched_hoods})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def profile(request, user_id):
    """
    Function that enables one to see their profile
    """
    title = "Profile"
    profiles = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'profile/profile.html',{'title':title,"profiles":profiles})

  
def new_profile(request):
    current_user = request.user
    profile=Profile.objects.get(user=request.user)
    hood= Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = ProfileForm()
    return render(request, "profile/edit_profile.html", {"form":form}) 
       

def business(request):
    """
    Function that enables one to see their profile
    """
    title = "Business"
    # businesses = User.objects.get(id=)
    user = User.objects.get(id=request.user.id)
    buss=Business.objects.all()
    return render(request, 'business/business.html',{'title':title,"buss":buss})

def new_business(request):
    current_user = request.user
    hood= Business.objects.all()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            form.save()
            return redirect('business')

    else:
        form = BusinessForm()
    return render(request, "business/edit_business.html", {"form":form}) 
       

def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.profile = current_user.profile
            hood.user = current_user

            hood.save()
        return redirect('hood')

    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {"form": form})       


@login_required(login_url='/registration/login/')
def join(request , hoodid):
    """
    This view edits neighbour class
    """
    this_neighbourhood =  NeighbourHood.objects.get(pk = hoodid)
    if Join.objects.filter(user = request.user).exists():
        Join.objects.filter(user_id = request.user).update(hood_id = this_neighbourhood.id)
    else:
        Join(user=request.user, hood_id = this_neighbourhood.id).save()
    messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('hood')


@login_required(login_url='/accounts/login/')
def exithood(request, id):
    """
    Allows users to exit hoods
    """
    Join.objects.get(user_id = request.user).delete()
    messages.error(request, "Neighbourhood exited")
    return redirect('hood')    