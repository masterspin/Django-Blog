from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
import operator
from django.db.models import Q
from django.views.generic import (
	ListView,
 	DetailView,
 	CreateView,
 	UpdateView,
 	DeleteView
 	)




def home(request):
	posts=Post.objects.all()
	query=request.GET.get("q")
	if query:
		posts = posts.filter(title__icontains=query)
	context = {
		'posts': posts
	}
	return render(request, 'courses/home.html', context)

@login_required
def myclasses(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'courses/myclasses.html', {'user_posts': logged_in_user_posts})


class PostListView(ListView):
	model = Post
	template_name = 'courses/home.html'
	context_object_name= 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'courses/user_posts.html'
	context_object_name= 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','description', 'main_Image', 'sub_Image_1', 'sub_Image_2']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','description', 'main_Image', 'sub_Image_1', 'sub_Image_2']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/myclasses/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'courses/about.html', {'title':'About'})


def first(request):
	return render(request, 'courses/first.html', {'title':'Welcome'})