from django.http import HttpResponse
from myapp.models import Movie
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    context_object_name = "my_list"
    template_name = "myapp/index.html"
    queryset = Movie.objects.all()

class MovieCreate(generic.CreateView):
    model = Movie
    fields = ['title','poster','director','year']
    template_name_suffix = '_form'
    success_url = reverse_lazy('myapp:main')

class MovieUpdate(generic.UpdateView):
    model = Movie
    fields = ['title','poster','director','year']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('myapp:main')

class MovieDelete(generic.DeleteView):
    model = Movie
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('myapp:main')

class MovieDetails(generic.DetailView):
    template_name_suffix = '_poster'
    queryset = Movie.objects.all()
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


