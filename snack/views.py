
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    context_object_name = "snacks"
    model  = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name= 'snack_create.html'
    fields=['title' , 'purchaser' , 'description']
    model = Snack
    success_url = reverse_lazy("snack_list")

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    fields=['title' , 'purchaser' , 'description']
    model = Snack
    


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")








    