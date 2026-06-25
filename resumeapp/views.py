from django.views.generic import TemplateView
from resumeapp.models import PersonData, SocialMedia, Cellphone,\
    Contact, Course, Experience, Education, Project, Technology, Document


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person_data"] = PersonData.objects.all()
        context["social_medias"] = SocialMedia.objects.all()
        context["cell_phones"] = Cellphone.objects.all()
        context["contacts"] = Contact.objects.all().filter(email__isnull=False)
        context["courses"] = Course.objects.all()
        context["experiences"] = Experience.objects.all()
        context["educations"] = Education.objects.all()
        context["projects"] = Project.objects.all()
        context["technologys"] = Technology.objects.all()
        context["documents"] = Document.objects.all()
        return context
