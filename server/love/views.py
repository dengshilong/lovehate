from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

class Index(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self):
        queryset = super(Index, self).get_queryset()
        queryset = queryset.select_related('category').order_by("-create_time")
        return queryset

class CreatePost(generic.CreateView):
    model = Post
    fields = ['cover']
    template_name = 'love/love_create.html'

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        obj = form.instance
        obj.user = self.request.user
        return super(CreatePost, self).form_valid(form)
