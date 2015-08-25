from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView

from apps.core.generics import MultiFormView
from .models import UserProfile
from .forms import UserForm, UserProfileForm


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

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            return HttpResponseRedirect(self.get_success_url())
        else:
            print user_form.errors, profile_form.errors

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'user_id': self.object.id})


class UserProfileView(DetailView):
    model = UserProfile
    template_name = "users/profile.html"
