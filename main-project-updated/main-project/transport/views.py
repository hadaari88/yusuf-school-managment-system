from django.shortcuts import render, get_object_or_404, redirect
from .models import Transport
from .forms import TransportForm

def transport_list(request):
    transports = Transport.objects.all()
    return render(request, 'transport/transport_list.html', {'transports': transports})

def transport_create(request):
    if request.method == "POST":
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport_list')
    else:
        form = TransportForm()
    return render(request, 'transport/transport_form.html', {'form': form})

def transport_update(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    if request.method == "POST":
        form = TransportForm(request.POST, instance=transport)
        if form.is_valid():
            form.save()
            return redirect('transport_list')
    else:
        form = TransportForm(instance=transport)
    return render(request, 'transport/transport_form.html', {'form': form})

def transport_delete(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    if request.method == "POST":
        transport.delete()
        return redirect('transport_list')
    return render(request, 'transport/transport_confirm_delete.html', {'transport': transport})
