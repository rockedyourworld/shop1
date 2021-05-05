from django.views.generic import ListView, DetailView

from posts.models import PostModel


class PostListView(ListView):
    template_name = 'blog.html'
    queryset = PostModel.objects.order_by('-pk')


class PostDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel
