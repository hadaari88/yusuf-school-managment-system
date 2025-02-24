from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fee
from .forms import FeeForm
class FeeListView(ListView):
    model = Fee
    template_name = 'fees/fee_list.html'
    context_object_name = 'fees'

class FeeCreateView(CreateView):
    model = Fee
    form_class = FeeForm
    template_name = 'fees/fee_form.html'
    success_url = reverse_lazy('fees:fee-list')

class FeeUpdateView(UpdateView):
    model = Fee
    form_class = FeeForm
    template_name = 'fees/fee_form.html'
    success_url = reverse_lazy('fees:fee-list')

class FeeDeleteView(DeleteView):
    model = Fee
    template_name = 'fees/fee_confirm_delete.html'
    success_url = reverse_lazy('fees:fee-list')
