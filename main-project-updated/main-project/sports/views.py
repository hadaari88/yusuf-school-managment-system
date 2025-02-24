from django.shortcuts import render, get_object_or_404, redirect
from .models import Sport
from .forms import SportForm

def sports_list(request):
    sports = Sport.objects.all()
    return render(request, 'sports/sports_list.html', {'sports': sports})

def sport_create(request):
    if request.method == "POST":
        form = SportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sports_list')
    else:
        form = SportForm()
    return render(request, 'sports/sport_form.html', {'form': form})

def sport_update(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    if request.method == "POST":
        form = SportForm(request.POST, instance=sport)
        if form.is_valid():
            form.save()
            return redirect('sports_list')
    else:
        form = SportForm(instance=sport)
    return render(request, 'sports/sport_form.html', {'form': form})

def sport_delete(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    if request.method == "POST":
        sport.delete()
        return redirect('sports_list')
    return render(request, 'sports/sport_confirm_delete.html', {'sport': sport})

