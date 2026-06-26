from django.contrib import admin
from .models import PersonData, Cellphone, SocialMedia, Contact, Course, Experience, Education, Project, Technology, Document


@admin.register(PersonData)
class PersonDataAdmin(admin.ModelAdmin):
    list_display = ["image", "firstname", "lastname", "birthday"]


@admin.register(Cellphone)
class CellphoneAdmin(admin.ModelAdmin):
    list_display = ["ddi", "cellphone"]


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ["link", "social_media_icon"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["person_data_id", "email", "cellphone_id", "social_media_id"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["course", "year", "duration", "situation", "education_institution", "minor"]


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
    list_display = ["technology", "project"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["description"]
