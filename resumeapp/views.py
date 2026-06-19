from django.views.generic import TemplateView
from resumeapp.models import PersonData, Contact, Course, Experience, Education, Project, Technology, Document


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person_data"] = PersonData.objects.all()
        context["contact"] = Contact.objects.all()
        context["experience"] = Experience.objects.all()
        context["education"] = Education.objects.all()
        context["project"] = Project.objects.all()
        context["technology"] = Project.objects.all()
        context["document"] = Project.objects.all()
        return context
