from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, FormView

from apps.core.generics import MultiFormView
from apps.core.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import UserForm, UserProfileForm, LoginForm


class CreateAccountView(MultiFormView):
    template_name = "users/register.html"
    form_classes = {
        'user_form': UserForm,
        'profile_form': UserProfileForm
    }

    success_url = 'users.profile'

    def post(self, request, *args, **kwargs):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            user_id = user.id

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            # Now we save the UserProfile model instance.
            profile.save()

            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)

            return HttpResponseRedirect(self.get_success_url(user_id))
        else:
            print (user_form.errors, profile_form.errors)

    def get_success_url(self, user_id):
        return reverse(self.success_url, kwargs={'pk': user_id})


class LoginView(FormView):
    form_class = LoginForm
    template_name = "users/login.html"

    success_url = 'homepage'

    def post(self, request, *args, **kwargs):
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(self.get_success_url())
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Mixees account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get('next', '')
        if redirect_to:
            return redirect_to
        return reverse(self.success_url)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('homepage'))


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = "users/profile.html"
