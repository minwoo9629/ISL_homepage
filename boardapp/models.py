from django.db import models
from django.conf import settings
from hitcount.models import HitCount, HitCountMixin
from django.contrib.auth.models import User
from datetime import datetime
from uuid import uuid4
# Create your models here.

def get_file_path(instance,filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/', ymd_path, uuid_name])

class DjangoBoard(models.Model,HitCountMixin):
      subject = models.CharField(max_length=50, null=True, verbose_name="과목")
      professor = models.CharField(max_length=10, null=True, verbose_name="교수")
      item = models.CharField(max_length=10, null=True, verbose_name="항목")
      title = models.CharField(max_length=50, null=True, verbose_name="글 제목")
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      year = models.IntegerField()
      hits = models.IntegerField(default=0)
      upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True)
      filename = models.CharField(max_length=64, null=True, verbose_name="파일 이름")


      def __str__(self):
          return self.subject
      
      @property
      def hit_update_counter(self):
          self.hits = self.hits + 1
          self.save()

# class DataRoom(models.Model):
#     subject = models.CharField(max_length=50, blank=True, verbose_name="과목")
#     professor = models.CharField(max_length=10,blank=True, verbose_name="교수")
#     item = models.CharField(max_length=10, verbose_name="항목")
#     title = models.CharField(max_length=50, blank=True, verbose_name="글 제목")
#     year = models.DateField()
#     author = models.CharField(max_length=50, blank=True, verbose_name="글 작성자")
#     upload_files = models.FileField(upload_to=get_file_path, null=True, blank=True)
#     filename = models.CharField(max_length=64, null=True, verbose_name="파일 이름")
    