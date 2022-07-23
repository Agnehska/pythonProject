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


# CRUD-операции
# (venv) C:\Users\Свешникова Анна\Desktop\pythonProject3\mysite>python manage.py shell
# Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from citizen.models import People
# >>> People(name='Петров Андрей', age='25', master='Иванов Иван')
# <People: Петров Андрей>
# >>> man1 = _
# >>> man1
# <People: Петров Андрей>
# >>> man1.name
# 'Петров Андрей'
# >>> man1.age
# '25'
# >>> man1.save()
# >>> man2 = People(name='Иванов Иван', age='25', master='')
# >>> man2.save()
# >>> man4 = People.objects.create(name='Artur', age='25', master='87')
# >>> People.objects.all()
# <QuerySet [<People: Anna Sveshnikova>, <People: Artur>, <People: Абрамов Аркадий>, <People: Авдеева Светлана>, <People: Агафонова Анна>, <People: Аксёнова Илена>, <People: Александров Арнольд>, <People: Александров Аскольд>, <People: А
# лександров Денис>, <People: Александров Роман>, <People: Александрова Георгина>, <People: Александрова Лили>, <People: Александрова Пелагея>, <People: Анисимова Тамара>, <People: Антипов Платон>, <People: Антонов Артур>, <People: Антон
# ова София>, <People: Апоян Давид>, <People: Ардаков Игорь>, <People: Архангельская Мария>, '...(remaining elements truncated)...']>
# >>> people = _
# >>> people
# <QuerySet [<People: Anna Sveshnikova>, <People: Artur>, <People: Абрамов Аркадий>, <People: Авдеева Светлана>, <People: Агафонова Анна>, <People: Аксёнова Илена>, <People: Александров Арнольд>, <People: Александров Аскольд>, <People: А
# лександров Денис>, <People: Александров Роман>, <People: Александрова Георгина>, <People: Александрова Лили>, <People: Александрова Пелагея>, <People: Анисимова Тамара>, <People: Антипов Платон>, <People: Антонов Артур>, <People: Антон
# ова София>, <People: Апоян Давид>, <People: Ардаков Игорь>, <People: Архангельская Мария>, '...(remaining elements truncated)...']>
# >>> for man in people:
# ...     print(man.name)
# ...
# Anna Sveshnikova
# Artur
# Абрамов Аркадий
# Авдеева Светлана
# Агафонова Анна
# Аксёнова Илена ……….
# >>> man = People.objects.get(name='Artur')
# >>> man.name='Артур'
# >>> man.save()
# >>> man = People.objects.get(name='Иванов Иван')
# >>> man.delete()