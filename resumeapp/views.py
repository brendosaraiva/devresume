from django.views.generic import TemplateView
from resumeapp.models import PersonData, Contact, Course, Experience, Education, Project, Technology, Document


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person_data"] = PersonData.objects.all()
        context["contacts"] = Contact.objects.all()
        context["experiences"] = Experience.objects.all()
        context["educations"] = Education.objects.all()
        context["projects"] = Project.objects.all()
        context["technologys"] = Project.objects.all()
        context["documents"] = Project.objects.all()
        return context
