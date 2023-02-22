from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ResumeList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True, )
    # CONTACT PART
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.TextField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    # SKILL PART
    skill_01 = models.CharField(max_length=20, null=True, blank=True)
    skill_02 = models.CharField(max_length=20, null=True, blank=True)
    skill_03 = models.CharField(max_length=20, null=True, blank=True)
    skill_04 = models.CharField(max_length=20, null=True, blank=True)
    skill_05 = models.CharField(max_length=20, null=True, blank=True)
    skill_06 = models.CharField(max_length=20, null=True, blank=True)
    # AWARDS PART
    award_01 = models.CharField(max_length=20, null=True, blank=True)
    award_02 = models.CharField(max_length=20, null=True, blank=True)
    award_03 = models.CharField(max_length=20, null=True, blank=True)
    award_04 = models.CharField(max_length=20, null=True, blank=True)
    award_05 = models.CharField(max_length=20, null=True, blank=True)
    # LANGUAGE PART
    language_01 = models.CharField(max_length=20, null=True, blank=True)
    language_02 = models.CharField(max_length=20, null=True, blank=True)
    # PROFILE PART
    title = models.TextField(max_length=200, null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)
    profile_detail = models.TextField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='Picture/', default='default.jpg', null=True, blank=True)
    # JOB EXPERIENCE PART
    job_title_01 = models.CharField(max_length=100, null=True, blank=True)
    j1_j_d = models.TextField(null=True, blank=True)
    j1_l_d = models.TextField(null=True, blank=True)
    job_details_01 = models.TextField(max_length=500, null=True, blank=True)
    job_title_02 = models.CharField(max_length=100, null=True, blank=True)
    j2_j_d = models.TextField(null=True, blank=True)
    j2_l_d = models.TextField(null=True, blank=True)
    job_details_02 = models.TextField(max_length=500, null=True, blank=True)
    job_title_03 = models.CharField(max_length=100, null=True, blank=True)
    j3_j_d = models.TextField(null=True, blank=True)
    j3_l_d = models.TextField(null=True, blank=True)
    job_details_03 = models.TextField(max_length=500, null=True, blank=True)
    # EDUCATION PART
    school = models.TextField(max_length=60, null=True, blank=True)
    s_j_d = models.TextField(null=True, blank=True)
    s_l_d = models.TextField(null=True, blank=True)
    college = models.TextField(max_length=60, null=True, blank=True)
    c_j_d = models.TextField(null=True, blank=True)
    c_l_d = models.TextField(null=True, blank=True)
    university = models.TextField(max_length=60, null=True, blank=True)
    u_j_d = models.TextField(null=True, blank=True)
    u_l_d = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
