from .models import Department,Specialty,MediaRecord,Feedback
from modeltranslation.translator import TranslationOptions, register


@register(Department)
class CourseTranslationOptions(TranslationOptions):
    fields = ('department_name',)

@register(Specialty)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('specialty_name',)


@register(MediaRecord)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('diagnosis','prescribed_medication','treatment' )

@register(Feedback)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('comment',)




