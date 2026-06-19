from django.contrib import admin
from .models import PersonData, Contact, Course, Experience, Education, Project, Technology, Document


@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ["image", "firstname", "lastname", "birthday"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "ddi", "cellphone", "social_media"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course", "duration", "education_institution", "minor"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["company", "start_date", "end_date", "activities"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["education", "start_date", "end_date", "description"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project", "description", "link"]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ["technology"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["description"]
