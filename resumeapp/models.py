from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator


def current_year():
    return date.today().year


class PersonData(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'fa-facebook'),
        ('twitter', 'fa-twitter'),
        ('linkedin', 'fa-linkedin'),
        ('instagram', 'fa-instagram'),
        ('github', 'fa-github'),
    ]
    firstname = models.CharField("Name", max_length=15)
    lastname = models.CharField("Last name", max_length=20)
    birth_day = models.DateTimeField(
        "Birthday",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ]
    )
    street = models.CharField("Street", max_length=30, blank=True, null=True)
    number = models.IntegerField("Number", blank=True, null=True)
    neighborhood = models.CharField("Neighborhood", blank=True, null=True)
    email = models.CharField("E-mail", max_length=50, blank=True, null=True)
    ddi = models.CharField("DDI", max_length=3, blank=True, null=True)
    cellphone = models.CharField("Number", max_length=13, blank=True, null=True)
    social_media = models.CharField(
        "Link",
        max_length=20,
        choices=SOCIAL_MEDIA_CHOICES,
        blank=True
    )

    def __str__(self):
        return self.firstname


class Course(models.Model):
    course = models.CharField("Course", max_length=150)
    duration = models.DurationField("Duration")
    education_institution = models.CharField("Education institution", max_length=30)
    minor = models.CharField("Minor", max_length=100)

    def __str__(self):
        return self.course


class Experience(models.Model):
    company = models.CharField("Company", max_length=150)
    start_date = models.DateTimeField(
        "Start date",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ]
    )
    end_data = models.DateTimeField(
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

    def __str__(self):
        return self.company


class Education(models.Model):
    education = models.CharField("Education", max_length=50)
    start_date = models.DateTimeField(
        "Start date",
        default=current_year,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year)
        ]
    )
    end_data = models.DateTimeField(
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

    def __str__(self):
        return self.education


class Document(models.Model):
    description = models.TextField("Description", max_length=250)

    def __str__(self):
        return self.description

