from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Comment
from .forms import PostForm,UpdateForm,CommentForm
# Create your views here.

#def blog_content(request):
#	return render(request, 'myblog/blog_content.html', {})

class blog_content(ListView):
	model = Post
	template_name = 'myblog/blog_content.html'

class blog_detail(DetailView):
	model = Post
	template_name = 'myblog/blog_detail.html'

class blog_add(CreateView):
	model = Post
	form_class = PostForm
	success_message = 'Post Added'
	template_name = 'myblog/blog_add.html'
	#fields = '__all__'
	#fields = ('title', 'author','body')

class blog_update(UpdateView):
	model = Post
	form_class = UpdateForm
	template_name = 'myblog/blog_update.html'
	#fields = ['title', 'body']

class blog_comment(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'myblog/blog_comment.html'
	#fields = '__all__'
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('blog_content')