from django.contrib import admin
from .models import Experiment, ExperimentComment
from .models import Person
from .models import Learning, LearningComment, LearningFromExperiment, LearningFromExperience
from .models import Experience, ExperienceComment, ExperimentBasedOnLearning, ExperimentBasedOnExperience

class LearningFromExperimentInline(admin.TabularInline):
    model = LearningFromExperiment
    extra = 0

class LearningFromExperienceInline(admin.TabularInline):
    model = LearningFromExperience
    extra = 0

class LearningCommentInline(admin.TabularInline):
    model = LearningComment
    extra = 0

class ExperimentBasedOnLearningInline(admin.TabularInline):
    model = ExperimentBasedOnLearning
    extra = 0

class ExperimentBasedOnExperienceInline(admin.TabularInline):
    model = ExperimentBasedOnExperience
    extra = 0

class ExperimentCommentInline(admin.TabularInline):
    model = ExperimentComment
    extra = 0

#
# Learning
#

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    inlines = [
        LearningFromExperimentInline,
        LearningFromExperienceInline,
        LearningCommentInline,
        ExperimentBasedOnLearningInline,
    ]


#
# Experiment
#

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster',)
    inlines = [
        ExperimentBasedOnLearningInline,
        ExperimentBasedOnExperienceInline,
        ExperimentCommentInline,
        LearningFromExperimentInline,
    ]


#
# Experience
#

class ExperienceCommentInline(admin.TabularInline):
    model = ExperienceComment
    extra = 0

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [
        ExperienceCommentInline,
        ExperimentBasedOnExperienceInline,
    ]


#
# Person
#

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

