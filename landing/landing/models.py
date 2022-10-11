import base64
import datetime
import os.path

from django.db import models
from django.utils.html import format_html
from .settings import BASE_DIR


class TeamMember(models.Model):
    member_id = models.IntegerField(auto_created=True, null=False, primary_key=True, editable=False)
    member_name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    avatar_name = models.ImageField(upload_to="images/", default='blank.jpg')
    avatar_b64 = models.BinaryField(null=True, editable=False)

    class Meta:
        db_table = "team_member"
        verbose_name_plural = 'Team Member'

    def __str__(self):
        return self.member_name

    def save(self, *args, **kwargs):
        if self.avatar_name:
            img_file = self.avatar_name.open()
            self.avatar_b64 = base64.b64encode(img_file.read())
            super(TeamMember, self).save(*args, **kwargs)
            for images in os.listdir(os.path.join(BASE_DIR, 'images')):
                os.remove(os.path.join(BASE_DIR, 'images', images))


class WorkExample(models.Model):
    work_id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=300, null=False)
    url = models.CharField(max_length=1000, null=True)
    avatar_name = models.ImageField(upload_to="images/", default='blank.jpg')
    avatar_b64 = models.BinaryField(null=True, editable=False)

    class Meta:
        db_table = "work_example"
        verbose_name_plural = 'Work Example'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.avatar_name:
            img_file = self.avatar_name.open()
            self.avatar_b64 = base64.b64encode(img_file.read())
            super(WorkExample, self).save(*args, **kwargs)
            for images in os.listdir(os.path.join(BASE_DIR, 'images')):
                os.remove(os.path.join(BASE_DIR, 'images', images))