from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie3.models import Jobs


class JobView(ListView):
    model = Jobs
    template_name = 'aplicatie3/jobs_index.html'

class CreateJobsView(LoginRequiredMixin,CreateView):
    model=Jobs
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'aplicatie3/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')

class UpadteJobView(LoginRequiredMixin,UpdateView):
    model = Jobs
    fields = ['type', 'url', 'title', 'description', 'how_to_apply']
    template_name = 'aplicatie3/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_joburi')
@login_required
def delete_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=0)
    return redirect('jobs:lista_joburi')
@login_required
def activate_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=1)
    return redirect('jobs:lista_joburi')