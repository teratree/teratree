from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Experience
from .forms import ExperienceForm

def home(request):
    context = {}
    return render(request, 'experiment/home.html', context)

def experience_index(request):
    experience_list = Experience.objects.order_by('-posted')
    context = {'experience_list': experience_list}
    return render(request, 'experiment/experience_index.html', context)

def experience_detail(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    return render(request, 'experiment/experience_detail.html', {'experience': experience})

def experience_create(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = Experience(**form.cleaned_data)
            experience.save()
            return redirect(reverse('experiment:experience-detail', kwargs={'experience_id': experience.id}))
    else:
        form = ExperienceForm()
    return render(request, 'experiment/experience_create.html', {
        'form': form,
    })

