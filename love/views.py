from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import generic
from .models import Post, Category


class Index(generic.ListView):
    model = Post
    paginate_by = 100

    def get_queryset(self):
        queryset = super(Index, self).get_queryset()
        queryset = queryset.select_related('category').order_by("-create_time")
        return queryset


class PostCreate(generic.CreateView):
    model = Post
    fields = ['cover']
    template_name = 'love/love_create.html'

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        name = self.request.POST.get('category')
        if not name:
            name = '无题'
        category = Category.objects.filter(name=name).first()
        if not category:
            category = Category(name=name)
            category.save()
        obj = form.instance
        obj.user = self.request.user
        obj.category = category
        return super(PostCreate, self).form_valid(form)


class CategoryList(generic.ListView):
    model = Post

    def get_queryset(self):
        cat = get_object_or_404(Category, name=self.kwargs['category'])
        queryset = Post.objects.filter(
            category=cat.id).order_by('-create_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context
