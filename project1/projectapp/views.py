from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import CustomLoginForm, StaffAddForm, SubmitForm, FeedbackEntryForm
from projectapp.models import CustomUser 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from .models import CustomUser, FeedbackProvider, Building, Category, FeedbackEntry
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm 
import logging

logger = logging.getLogger(__name__)
# Create your views here
def Index(request):
    return render(request, 'registration/index.html', {'section': 'index'})

def About(request):
    return render(request, 'registration/about.html', {'section': 'about'})

def feedback_form(request):
    thank_you_flag = False
    print(request.POST)  # Check if the form data is being received
    print(request.FILES)
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        entry_form = FeedbackEntryForm(request.POST, request.FILES)

        if form.is_valid() and entry_form.is_valid():
            feedback_provider = form.save(commit=False)

            # Check if the user chose to submit anonymously
            is_anonymous_str = request.POST.getlist('is_anonymous', ['False'])[0]
            is_anonymous = is_anonymous_str.lower() == 'true'

            if is_anonymous:
                feedback_provider.first_name = 'Anonymous'
                feedback_provider.last_name = 'Anonymous'
                feedback_provider.is_anonymous = True
            else:
                feedback_provider.is_anonymous = False

            feedback_provider.save()

            # Now, create a FeedbackEntry using the submitted data
            feedback_entry = entry_form.save(commit=False)
            feedback_entry.provider = feedback_provider
            feedback_entry.building_id = form.cleaned_data['building_id']
            feedback_entry.category_id = form.cleaned_data['category_id']

            feedback_entry.save()

            # Set the thank_you_flag to True
            thank_you_flag = True

    else:
        form = SubmitForm()  # Moved outside the if block
        entry_form = FeedbackEntryForm()

    # Fetch the selected building from the form data
    building_id = request.GET.get('building', None)

    # If building_id is not present or is not a valid integer, set a default
    building_id = int(building_id) if building_id and building_id.isdigit() else 2

    # Fetch categories for the selected building
    categories = Category.objects.filter(building_id=building_id)

    buildings = Building.objects.all()

    return render(request, 'registration/feedbackform.html', {
        'form': form,
        'entry_form': entry_form,
        'buildings': buildings,
        'categories': categories,
        'selected_building_id': building_id,
        'selected_category_id': request.GET.get('category', None),
        'thank_you_flag': thank_you_flag,
    })
def get_categories_by_building(request):
    building_id = request.GET.get('building_id', None)
    print(f"Received building_id: {building_id}")

    if building_id:
        categories = Category.objects.filter(building_id=building_id).values('category_id', 'category_name')
        print(f"Categories for building {building_id}: {categories}")
        return JsonResponse({'categories': list(categories)})

    return JsonResponse({'categories': []})
 
def is_superuser(user):
    return user.is_superuser
@login_required
@user_passes_test(is_superuser)
def admin_dashboard(request):
    users = CustomUser.objects.filter(is_staff=False)
    if request.method == 'POST':
        form = StaffAddForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = False  # Set the user as staff
            user.save()
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
    else:
        form = StaffAddForm()
    context = {
        'users': users,  # Pass the list of user objects to the template context
        'form':form,
    }
    return render(request, 'registration/admin_dashboard.html', context )
def is_not_superuser(user):
    return not user.is_superuser
@login_required
@user_passes_test(is_not_superuser)
def mydashboard(request):
    
    print(request.user)
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})

class CustomLoginView(LoginView):
     form_class = CustomLoginForm  # Use the CustomLoginForm
     def form_invalid(self, form):
        # Check if the reCAPTCHA checkbox was checked
        captcha_response = form.cleaned_data.get('captcha')
        if not captcha_response:
            messages.error(self.request, 'Please check the reCAPTCHA below.')
            return super().form_invalid(form)

        # Check if the user exists in the database and the password is incorrect
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(self.request, 'Incorrect username or password. Please try again.')
            return super().form_invalid(form)

        messages.error(self.request, 'Please check the reCAPTCHA below.')
        return super().form_invalid(form)

     def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse ('admin_dashboard')  # Redirect superuser to the admin site
        else:
            return reverse ('dashboard')  # Redirect other users to the dashboard
def login(request):
    return render(request, 'login.html', {'section': 'login'})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'passwordchange.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        messages.success(self.request, 'Password successfully changed.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Password change failed. Please correct the errors below.')
        return super().form_invalid(form)

def logout_user(request):
    #A message when logout
    messages.success(request, "Successfully logged out.")

    #Log out the user
    logout(request)

    #Redirect to the login html
    return redirect('index')
'''
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']

            # Check if an existing user with the same email address exists
            if User.objects.filter(email=email).exists():  
                messages.error(request, 'Email address is already in use.')
            else:
                # Create a new user but avoid saving it
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password1'])
                # Save the user object
                new_user.save()
                messages.success(request, 'Account created successfully. You can log in now.')
                return redirect('dashboard')  # Redirect to the dashboard or another page after successful signup
        else:
            # Clear existing messages
            # Add error messages for the specific form field errors with a 'signup_error' tag
            messages.error(request, 'Please correct the errors below.', 'signup_error')
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}", 'signup_error')

    else:
        user_form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'user_form': user_form})
'''
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

def add_staff(request):
    if request.method == 'POST':
        form = StaffAddForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = False  # Set the user as staff
            if 'profile_image' in request.FILES:  # Check if a file is uploaded
                user.profile_image = request.FILES['profile_image']
            user.save()
            return redirect('admin_dashboard')
    else:
        form = StaffAddForm()
    return render(request, 'admin_dashboard.html', {'form': form})

def remove_staff_members(request):
    if request.method == "POST":
        user_ids = request.POST.getlist("user_ids[]")  # Get the selected user IDs

        # Implement the logic to remove staff members based on user IDs
        try:
            # Convert the received user IDs to integers
            user_ids = [int(user_id) for user_id in user_ids]
            
            # Use the User model to delete users with the given IDs
            CustomUser.objects.filter(id__in=user_ids).delete()
            
            return JsonResponse({"message": "Staff members removed successfully"})
        except ValueError:
            return JsonResponse({"error": "Invalid user IDs provided"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=400)

