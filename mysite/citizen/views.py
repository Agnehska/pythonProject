from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q
from .filters import ProductFilter

# class Men(ListView):
#     model = People
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
#         return context

def citizens(request):
   search_query = request.GET.get('search', '')
   if search_query:
       people = People.objects.filter(Q(name__icontains=search_query) | Q(age__icontains=search_query) | Q(master__icontains=search_query) )
   else:
       people = People.objects.all()
   return render(request, 'citizen/citizen.html', {'people': people})


class ManDetailView(DetailView):
    model = People
    template_name = 'citizen/details_view.html'
    context_object_name = 'man'

class ManUpdateView(UpdateView):
    model = People
    template_name = 'citizen/update.html'

    form_class = PeopleForm

class ManDeleteView(DeleteView):
    model = People
    success_url = '/'
    template_name = 'citizen/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('citizens')
        else:
            error = 'Данные введены не верно'
    if request.method == 'POST':
        form2 = StatusForm(request.POST)
        if  form2.is_valid():
            form2.save()
            return redirect('citizens')
        else:
            error = 'Данные введены не верно'
    form = PeopleForm()
    form2 = StatusForm()
    data = {
        'form': form,
        'form2': form2,
        'error': error,
    }
    return render(request, 'citizen/create.html', data)

def product_list(request):
    filter = ProductFilter(request.GET, queryset=People.objects.all())
    return render(request, 'citizen/citizen.html', {'filter': filter})