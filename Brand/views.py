from django.shortcuts import render,redirect 
from .import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.contrib.auth import login,logout
from .forms import registerForm, BrandForm,CarForm
from django.views.generic import FormView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import TemplateView



class UserLoginView(LoginView):
   template_name = 'login.html'
   def get_success_url(self):
      return reverse_lazy('home')


class userRegistrationView(FormView):
   template_name="login.html"
   form_class = registerForm
   success_url = reverse_lazy('home')
   
   def form_valid(self,form):
      user = form.save()
      login(self.request, user)
      return super().form_valid(form)
   
login_required(login_url='Car/')
def User_Logout(request):
     logout(request)
     return redirect('home')


class BrandRegistrationView(FormView):
   template_name="login.html"
   form_class =  forms.BrandForm
   success_url = reverse_lazy('home')
   
   def form_valid(self,form):
      musician = form.save(commit=False)
      musician.save()
      return super().form_valid(form)
   


class DetailCarView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'detailspage.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@login_required
def buy_car(request, id):
    car = Car.objects.get(id=id)
    if car.quantity > 0:
        order = Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
        return redirect('profile')
    else:
        return render(request, 'car_detail.html', {'car': car, 'error': 'This car is out of stock'})


@login_required
def edit_profile(request):
    
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'login.html', {'form' : profile_form})


login_required(login_url='Car/')
class ProfileView(TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        return context
    



