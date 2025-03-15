from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q


from .models import Kanji
from .forms import KanjiForm


def kanji_list(request):
    query = request.GET.get('q')

    if query:
        kanji_list = Kanji.objects.filter(
            Q(character__icontains=query) | 
            Q(english_translation__icontains=query)
        )
    else:
        kanji_list = Kanji.objects.all()
    return render(request, 'kanji_list.html', {'kanji_list': kanji_list})


def kanji_detail(request, pk):
    kanji = get_object_or_404(Kanji, pk=pk)
    return render(request, 'kanji_detail.html', {'kanji': kanji})

def kanji_create(request):
    if request.method == "POST":
        form = KanjiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanji_list')
    else:
        form = KanjiForm()
    return render(request, 'kanji_form.html', {'form': form})

def kanji_update(request, pk):
    kanji = get_object_or_404(Kanji, pk=pk)
    if request.method == "POST":
        form = KanjiForm(request.POST, instance=kanji)
        if form.is_valid():
            form.save()
            return redirect('kanji_detail', pk=kanji.pk)
    else:
        form = KanjiForm(instance=kanji)
    return render(request, 'kanji_form.html', {'form': form})

def kanji_delete(request, pk):
    kanji = get_object_or_404(Kanji, pk=pk)
    if request.method == "POST":
        kanji.delete()
        return redirect('kanji_list')
    return render(request, 'kanji_confirm_delete.html', {'kanji': kanji})