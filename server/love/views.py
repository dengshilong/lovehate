from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic
from .models import Post, Category

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

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        name = self.request.POST.get('category', '无题')
        category = Category.objects.filter(name=name).first()
        if not category:
            category = Category(name=name)
            category.save()
        obj = form.instance
        obj.user = self.request.user
        obj.category = category
        return super(CreatePost, self).form_valid(form)
