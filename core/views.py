from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from core.models import Block, Convict
from django.db.models import Q


class Home(ListView):
    model=Block
    template_name='core/home.html'

class CreateConvict(CreateView):
    model=Convict
    fields=['name', 'aliases', 'gender', 'place_of_birth', 'date_of_birth', 'education', 'financial_background']
    success_url=reverse_lazy('home')
    template_name='core/createconvict.html'

class CreateBlock(CreateView):
    model=Block
    fields=['perp', 'charges', 'charges_code', 'known_accomplices', 'fir_date', 'conviction_date', 'comments','sentencer', 'sentence',]
    success_url=reverse_lazy('home')
    template_name='core/createblock.html'

class SearchView(ListView):
    model=Convict
    template_name='core/search.html'
    context_object_name='convicts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# Call the base implementation first to get a context
        convict_id=self.request.GET.get("searchstring")
        convict_name=self.request.GET.get("searchstring")
        crime_id=self.request.GET.get("searchstring")


        context['convict_id'] = self.request.GET.get("convict_id")
        context['convict_name'] = self.request.GET.get("convict_name")
        context['crime_id'] = self.request.GET.get("crime_id")

        if convict_name and crime_id:

            q=Block.objects.filter(
                Q(perp=convict_name) & Q(pk=crime_id)
            )
            context['qset']=q

        if convict_id and crime_id:

            q=Block.objects.filter(
                Q(perp=convict_name) & Q(pk=crime_id)
            )
            context['qset']=q

        #if type(context['convict_id'])

        return context

    def get_queryset(self):  # new
        query=self.request.GET.get("convict_id")
        convict_id=self.request.GET.get("searchstring")
        convict_name=self.request.GET.get("searchstring")
        crime_id=self.request.GET.get("searchstring")
        

        object_list = Convict.objects.filter(
            Q(pk=query) | Q(name__icontains=query)| Q(aliases__icontains=query)
        )
        return object_list




# Create your views here.
