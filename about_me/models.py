from django.db import models
from team_member.models import TeamMember
from core.models import Skills
from core.utils import image_delete_os, previous_image_delete_os, compress_image

class AboutMe(models.Model):
    person = models.OneToOneField(TeamMember, on_delete=models.CASCADE)
    short_description = models.TextField(blank=True, null=True)
    details_description = models.TextField(blank=True, null=True)
    resume_description = models.TextField(blank=True, null=True)
    testimonials_description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'About Me - {self.person}'

class SliderTagList(models.Model):
    aboutme = models.ForeignKey(AboutMe, on_delete=models.CASCADE, related_name="slider_tags")
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.aboutme.person.name} - {self.title}"

class Education(models.Model):
    Degree = (
        ('SSC','SSC'),
        ('HSC','HSC'),
        ('Diploma','Diploma'),
        ('BSC','BSC'),
        ('Other','Other'),
    )
    degree_name = models.CharField(max_length=25, choices=Degree)
    subject = models.CharField(max_length=50, blank=True, null=True)
    result = models.FloatField(max_length=4, blank=True, null=True)
    institute_name = models.CharField(max_length=200)
    institute_address = models.TextField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    cgpa = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_complete = models.BooleanField(default=True, blank=True, null=True)

    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.degree_name}'

class Certification(models.Model):
    course_name = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    institute_name = models.CharField(max_length=200)
    institute_address = models.TextField(blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_complete = models.BooleanField(default=True, null=False, blank=False)

    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.course_name} - {self.team_member}'

class Experience(models.Model):
    designation = models.CharField(max_length=30)
    company_name = models.CharField(max_length=40)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.company_name} - {self.designation}'

class MyWork(models.Model):
    member = models.ManyToManyField(TeamMember)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    industry = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    project_value = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    link =  models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MyWorkPicture(models.Model):
    work = models.ForeignKey(MyWork, on_delete=models.CASCADE, related_name='myworkpicture')
    image = models.ImageField(upload_to='work/me/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def get_image_optimized(self, new_image, old_image=None):
        if new_image and new_image != old_image and hasattr(new_image, "file"):
            return compress_image(new_image)
        return None

    def image_optimization(self, instance=None):
        image = self.get_image_optimized(self.image, instance.image if instance is not None else None)
        if image:
            self.image = image

    def image_update(self, instance):
        previous_image_delete_os(instance.image, self.image)

    def delete(self, *args, **kwargs):
        image_delete_os(self.image)
        return super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            instance = MyWorkPicture.objects.get(pk=self.pk)
            self.image_update(instance)
            self.image_optimization(instance)
        else:
            self.image_optimization()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Picture for #{self.pk} ({self.work.title})"

class Testimonials(models.Model):
    person_name = models.CharField(max_length=300, blank=True, null=True)
    person_designation = models.CharField(max_length=300, blank=True, null=True)
    opinion = models.TextField(blank=True, null=True)
    is_team = models.BooleanField(default=True, blank=True, null=True)
    is_me = models.BooleanField(default=True, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"Team Testimonials"
