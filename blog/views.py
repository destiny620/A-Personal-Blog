from django.shortcuts import render
from .models import BlogPost, Profile
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy


# Create your views here.


class blogsView(ListView):
    model = BlogPost
    template_name = 'index.html'
    ordering = ['-created_at']
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context

def Blog_Detail(request, slug):
    posts = BlogPost.objects.get(slug=slug)
    return render(request, 'blog_detail.html', {'posts': posts})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})


class EditProfileView(UpdateView):
    model = Profile
    form_class = Editprofileform
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    
    def get_object(self, queryset=None):
        # ensure the logged-in user always has a Profile instance
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class AddBlogPostView(CreateView):
    model = BlogPost
    form_class = BlogpostForm
    template_name = 'add_blogpost.html'
    success_url = reverse_lazy('blogsView')

class AddProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'add_profile.html'
    success_url = reverse_lazy('blogsView')

class EditBlogPostView(UpdateView):
    model = BlogPost
    form_class = EditBlogPostform
    template_name = 'edit_blogpost.html'
    success_url = reverse_lazy('blogsView')


class DeleteBlogPostView(DeleteView):
    model = BlogPost
    template_name = 'delete_blogpost.html'
    success_url = reverse_lazy('blogsView')

class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'delete_profile.html'
    success_url = reverse_lazy('blogsView')

# <section class="container-fluid bg-dark" id="about">
#    <h3 class="text-light disply-1 text-center pt-4">Discover Our Identity</h3>
    
#     <div class="row g-4 align-items-center">
#         <div class="col-md-5">
#      <img src="{% static "codexio_main/images/coding-group.png" %}" class="img-fluid rounded" alt="Programmers">
#         </div>
#         <div class="col-md-7">   m,.
#             <p>We unite programmers, fostering a supportive community. Our purpose is to empower aspiring talents, enlighten newcomers, and create programming gurus.</p>
#             <div class="learn-more-div">