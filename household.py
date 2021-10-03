from barkasse.models import Household
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HHMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hh'] = self.request.resolver_match.kwargs['hh']
        context['hh_name'] = Household.objects.get(id=self.request.resolver_match.kwargs['hh'])
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_url, args=[self.request.resolver_match.kwargs['hh']])


class HHListView(LoginRequiredMixin, HHMixin, ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(household=self.request.resolver_match.kwargs['hh'])


class HHCreateView(LoginRequiredMixin, HHMixin, CreateView):
    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.household = Household.objects.get(id=self.request.resolver_match.kwargs['hh'])
        object.save()
        return super(HHCreateView, self).form_valid(form)

class HHUpdateView(LoginRequiredMixin, HHMixin, UpdateView):
    pass


class HHDeleteView(LoginRequiredMixin, HHMixin, DeleteView):
    pass