# from django.contrib import admin
# from .models import Experience, ExperienceComment
# from .models import Experiment, ExperimentComment, ExperimentRelatedExperience
# from .models import Person
# 
# 
# class ExperimentRelatedExperienceInline(admin.TabularInline):
#     model = ExperimentRelatedExperience
#     extra = 0
# 
# class ExperimentCommentInline(admin.TabularInline):
# 
#     model = ExperimentComment
#     extra = 0
# 
# #
# # Experiment
# #
# 
# @admin.register(Experiment)
# class ExperimentAdmin(admin.ModelAdmin):
#     list_display = ('hypothesis', 'poster', 'importance', 'cost', 'time_required', 'data_reliability', 'action_required')
#     inlines = [
#         ExperimentCommentInline,
#         ExperimentRelatedExperienceInline,
#     ]
# 
# 
# #
# # Experience
# #
# 
# class ExperienceCommentInline(admin.TabularInline):
#     model = ExperienceComment
#     extra = 0
# 
# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     inlines = [
#         ExperienceCommentInline,
#         ExperimentRelatedExperienceInline,
#     ]
# 
# 
# #
# # Person
# #
# 
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email')
