from barkasse.models import Household, Member
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class HHMixin(LoginRequiredMixin, UserPassesTestMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hh'] = self.request.resolver_match.kwargs['hh']
        context['hh_name'] = Household.objects.get(id=self.request.resolver_match.kwargs['hh'])
        return context

    def get_success_url(self):
        return reverse_lazy(self.reverse_url, args=[self.request.resolver_match.kwargs['hh']])

    def test_func(self):
        return Member.objects.filter(household=self.request.resolver_match.kwargs['hh'], user=self.request.user)


class HHListView(HHMixin, ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(household=self.request.resolver_match.kwargs['hh'])


class HHCreateView(HHMixin, CreateView):
    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.household = Household.objects.get(id=self.request.resolver_match.kwargs['hh'])
        object.save()
        return super(HHCreateView, self).form_valid(form)

class HHUpdateView(HHMixin, UpdateView):
    pass


class HHDeleteView(HHMixin, DeleteView):
    pass