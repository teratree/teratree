# from django.shortcuts import render
# 
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse
# 
# from .models import ExperiencePage
# from .forms import ExperienceForm
# 
# def experience_index(request):
#     experience_list = ExperiencePage.objects.order_by('-posted')
#     context = {'experience_list': experience_list}
#     return render(request, 'experience/experience_index.html', context)
# 
# def experience_detail(request, experience_id):
#     experience = get_object_or_404(ExperiencePage, pk=experience_id)
#     return render(request, 'experience/experience_detail.html', {'experience': experience})
# 
# def experience_create(request):
#     if request.method == 'POST':
#         form = ExperienceForm(request.POST, request.FILES)
#         if form.is_valid():
#             experience = ExperiencePage(**form.cleaned_data)
#             experience.save()
#             return redirect(reverse('experience:experience-detail', kwargs={'experience_id': experience.id}))
#     else:
#         form = ExperienceForm()
#     return render(request, 'experience/experience_create.html', {
#         'form': form,
#     })
