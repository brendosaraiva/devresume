from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from stdimage import StdImageField


def current_year():
    return date.today().year


class PersonData(models.Model):
    image = StdImageField(
        "Photo",
        upload_to="img",
        variations={
            "thumbnail": (250, 250)
        },
        delete_orphans=True,
        blank=True

    )
    firstname = models.CharField("Name", max_length=15)
    lastname = models.CharField("Last name", max_length=20)
    birthday = models.DateField(
        "Birthday",
        default=current_year,
        validators=[
            MinValueValidator(date(1990, 1, 1)),
            MaxValueValidator(date.today)
        ]
    )

    class Meta:
        verbose_name = "Person data"
        verbose_name_plural = "Persons data"

    def __str__(self):
        return self.firstname


# Criar uma nova tabela para redes sociais e telefone (1FN)
class Contact(models.Model):
    person_data = models.ForeignKey(PersonData, on_delete=models.CASCADE)
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'fa-facebook'),
        ('twitter', 'fa-twitter'),
        ('linkedin', 'fa-linkedin'),
        ('instagram', 'fa-instagram'),
        ('github', 'fa-github'),
    ]
    email = models.CharField("E-mail", max_length=50, blank=True, null=True)
    ddi = models.CharField("DDI", max_length=3, blank=True, null=True)
    cellphone = models.CharField("Number", max_length=13, blank=True, null=True)
    link = models.CharField("Link rede social", max_length=60, blank=True, null=True)
    social_media_icon = models.CharField(
        "Link",
        max_length=20,
        choices=SOCIAL_MEDIA_CHOICES,
        blank=True
    )

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email


class Course(models.Model):
    course = models.CharField("Course", max_length=150)
    duration = models.DurationField("Duration")
    education_institution = models.CharField("Education institution", max_length=30)
    minor = models.CharField("Minor", max_length=100)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course


class Experience(models.Model):
    company = models.CharField("Company", max_length=150)
    start_date = models.IntegerField(
        "Start date",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ]
    )
    end_date = models.IntegerField(
        "End date",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ],
        blank=True,
        null=True
    )
    activities = models.TextField("Activities", max_length=250)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.company


class Education(models.Model):
    education = models.CharField("Education", max_length=50)
    start_date = models.IntegerField(
        "Start date",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ]
    )
    end_date = models.IntegerField(
        "End date",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ],
        blank=True,
        null=True
    )
    description = models.TextField("Description", max_length=250)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return self.education


class Project(models.Model):
    project = models.CharField("Project", max_length=50)
    description = models.TextField("Description", blank=True)
    link = models.URLField("Link", max_length=500)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.project


class Technology(models.Model):
    TECHNOLOGY_CHOICES = [
        # Linguagens de programação
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("typescript", "TypeScript"),
        ("java", "Java"),
        ("csharp", "C#"),
        ("cpp", "C++"),
        ("c", "C"),
        ("php", "PHP"),
        ("ruby", "Ruby"),
        ("go", "Go"),
        ("rust", "Rust"),
        ("kotlin", "Kotlin"),
        ("swift", "Swift"),
        ("dart", "Dart"),

        # Front-end
        ("html", "HTML"),
        ("css", "CSS"),
        ("sass", "Sass"),
        ("bootstrap", "Bootstrap"),
        ("tailwind", "Tailwind CSS"),
        ("react", "React"),
        ("angular", "Angular"),
        ("vue", "Vue.js"),
        ("svelte", "Svelte"),

        # Back-end Frameworks
        ("django", "Django"),
        ("flask", "Flask"),
        ("fastapi", "FastAPI"),
        ("nodejs", "Node.js"),
        ("express", "Express.js"),
        ("nestjs", "NestJS"),
        ("spring", "Spring Boot"),
        ("laravel", "Laravel"),
        ("aspnet", "ASP.NET"),

        # Banco de Dados
        ("mysql", "MySQL"),
        ("postgresql", "PostgreSQL"),
        ("sqlite", "SQLite"),
        ("mongodb", "MongoDB"),
        ("redis", "Redis"),
        ("oracle", "Oracle Database"),
        ("sqlserver", "SQL Server"),

        # Mobile
        ("android", "Android Native"),
        ("ios", "iOS Native"),
        ("flutter", "Flutter"),
        ("react_native", "React Native"),

        # Desktop
        ("qt", "Qt"),
        ("electron", "Electron"),
        ("tkinter", "Tkinter"),
        ("wpf", "WPF"),
        ("javafx", "JavaFX"),

        # Ciência de Dados / IA
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("scikit", "Scikit-Learn"),
        ("tensorflow", "TensorFlow"),
        ("pytorch", "PyTorch"),
        ("keras", "Keras"),
        ("opencv", "OpenCV"),

        # DevOps / Infraestrutura
        ("linux", "Linux"),
        ("docker", "Docker"),
        ("kubernetes", "Kubernetes"),
        ("terraform", "Terraform"),
        ("ansible", "Ansible"),
        ("jenkins", "Jenkins"),
        ("github_actions", "GitHub Actions"),

        # Controle de versão
        ("git", "Git"),
        ("github", "GitHub"),
        ("gitlab", "GitLab"),
        ("bitbucket", "Bitbucket"),

        # Cloud
        ("aws", "Amazon Web Services"),
        ("azure", "Microsoft Azure"),
        ("gcp", "Google Cloud Platform"),

        # CMS
        ("wordpress", "WordPress"),
        ("drupal", "Drupal"),
        ("joomla", "Joomla"),

        # Game Development
        ("unity", "Unity"),
        ("unreal", "Unreal Engine"),
        ("godot", "Godot"),

        # IoT / Hardware
        ("arduino", "Arduino"),
        ("raspberry", "Raspberry Pi"),
        ("esp32", "ESP32"),

        # Segurança
        ("kali", "Kali Linux"),
        ("wireshark", "Wireshark"),
        ("metasploit", "Metasploit"),

        # Outros
        ("uml", "UML"),
        ("api_rest", "REST API"),
        ("graphql", "GraphQL"),
        ("websocket", "WebSocket"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    technology = models.CharField(
        max_length=50,
        choices=TECHNOLOGY_CHOICES
    )

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.technology


class Document(models.Model):
    description = models.TextField("Description", max_length=250)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.description

