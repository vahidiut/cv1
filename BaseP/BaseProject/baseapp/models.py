import time

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
PRIORITIES = (
    ('انفجار','انفجار'),
    ('ESD', 'ESD'),
    ('normal stop','NORMAL STOP'),
    ('تاخیر در راه اندازی','تاخیر در راه اندازی'),
    ('موارد دیگر','موارد دیگر'),
)
RESPONSIBLES = (
    ('رئیس بهره بردار','رئیس بهره برداری'),
    ('سرپرست نوبتکارا','سرپرست نوبتکاران'),
    ('نوبتکار ارشد','نوبتکار ارشد'),
    ('نوبتکار','نوبتکار'),
)
SCORES = (
    (1 , 'refered to process'),
    (2 , 'refered to equipment manipulation'),
    (3 , 'refered to human safty'),
)

class Tasks(models.Model):
      task_creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
      task_id = models.IntegerField(default=0, unique=False, null=False)
      task_name = models.CharField(max_length=264, unique=False)
      task_priority = models.CharField(max_length=20, choices=PRIORITIES, default='explosion')
      task_responsible = models.CharField(max_length=20, choices=RESPONSIBLES, default='2')
      task_score = models.IntegerField(choices=SCORES,default=1)
      creation_date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)
      amendment_condition = models.BooleanField(default=False)
      def __str__(self):
         return '%s %s' % (self.task_id, self.task_name)

class SubTasks1(models.Model):
      related_task = models.ForeignKey('Tasks',on_delete=models.CASCADE, null=False, blank=False)
      subtask1_id = models.IntegerField(default=1, unique=True)
      subtask1_name = models.CharField(max_length=264, unique=False, default='زیروظیفه')
      subtask1_priority = models.CharField(max_length=20, choices=PRIORITIES, default='explosion')
      subtask1_responsible = models.CharField(max_length=20, choices=RESPONSIBLES, default='2')
      property_score = models.IntegerField(choices=SCORES,default=1)
      subtask1_creator = models.ForeignKey(User, on_delete=models.CASCADE, default="")
      creation_date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)
      number_of_verified_experiences = models.PositiveIntegerField(default=0, unique=False)
      number_of_submitted_experiences = models.PositiveIntegerField(default=0, unique=False)
      amendment_condition = models.BooleanField(default=False)
      def __str__(self):
          return '%s %s' % (self.subtask1_id, self.subtask1_name)

class Properties(models.Model):
      related_subtask1 = models.ForeignKey('SubTasks1', on_delete=models.CASCADE)
      experience = models.TextField(" تجربه مرتبط ")
      documents = models.TextField(" مدارک مرتبط ",default="مدارک تجهیزات مرتبط")
      property_score = models.IntegerField(choices=SCORES,default=1)
      experience_creator = models.ForeignKey(User, on_delete=models.CASCADE, default="")
  #    experience_evaluator = models.ForeignKey(User, on_delete=models.CASCADE, default="")
      creation_date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)
      amendment_condition = models.BooleanField(default=False)

      def __str__(self):
          return '%s %s' % (self.related_subtask1.subtask1_name, self.related_subtask1.related_task)

class Questions(models.Model):
      related_subtask1 = models.ForeignKey('SubTasks1', on_delete = models.CASCADE, null=True)
      question = models.TextField(" سوال مرتبط ")
      correct_answer = models.TextField(" پاسخ صحیح ")
      wrong_answer1 = models.TextField(" گزینه غلط اول ")
      wrong_answer2 = models.TextField(" گزینه غلط دوم ")
      wrong_answer3 = models.TextField(" گزینه غلط سوم ")
      question_explaination = models.TextField(" توضیحات مرتبط ", null=True, blank=True)
      question_score = models.IntegerField(choices=SCORES,default=1)
      question_creator = models.ForeignKey(User, on_delete=models.CASCADE, default="")
      creation_date = models.DateField(auto_now_add=True, null=True, blank=True, editable=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_score = models.FloatField(default=0, unique=False, null=False)

    number_of_new_tasks = models.PositiveIntegerField(default=0, unique=False)
    number_of_repeated_tasks = models.PositiveIntegerField(default=0, unique=False)

    number_of_new_subtask1s = models.PositiveIntegerField(default=0, unique=False)
    number_of_repeated_subtask1s = models.PositiveIntegerField(default=0, unique=False)

    number_of_new_experiences = models.PositiveIntegerField(default=0, unique=False)
    number_of_repeated_experiences = models.PositiveIntegerField(default=0, unique=False)

    number_of_new_submitted_questions = models.PositiveIntegerField(default=0, unique=False)
    number_of_repeated_submitted_questions = models.PositiveIntegerField(default=0, unique=False)



'''
class Users(AbstractUser):
    pass

class UserInfo(AbstractBaseUser):
#    user_id = models.IntegerField()
#    user = models.CharField(max_length=256, blank=True)
#    user_category = models.CharField(max_length=20, choices=RESPONSIBLES, default='2')

    username = models.CharField(max_length=16,primary_key=False)
#    user = models.OneToOneField(
#    User,
#    on_delete=models.CASCADE,
#    )

    #portfolio = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pic', blank=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
'''
#from django.contrib.auth.models import AbstractUser

'''
class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
'''
