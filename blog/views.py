from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
            'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    comments = Comment.objects.filter(post=post).order_by('-created_date')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment_form = Comment.objects.create(post=post,author = request.user,text = text)
            comment_form.save()
            return redirect('post-detail',pk = post.pk)
    else:
        comment_form = CommentForm()
    content={'post':post,
             'comments':comments,
             'comment_form':comment_form
              }
    return render(request,'blog/post_detail.html',content)
