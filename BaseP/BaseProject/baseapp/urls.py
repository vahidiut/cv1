from django.urls import path
from baseapp import views

app_name = 'baseapp'

urlpatterns=[
path('newtask/<int:task_id>',views.newtask,name='newtask'),
path('taskpage/<int:task_id>/newsubtask1/<int:subtask1_id>',views.newsubtask1,name='newsubtask1'),
path('tasks/',views.list,name='tasks'),
path('<int:task_id>/newproperty/<int:subtask1_id>',views.task_property,name='tasks_properties'),

path('<int:task_id>/newquestion/<int:subtask1_id>',views.subtask1_questions,name='new_questions'),

#path('accounts/signup/',views.signup_view,name='signup'),
#path('logout/', views.logout_request, name="logout"),
#path('accounts/login/', views.login_request, name="login"),

path('taskpage/<int:id>/', views.taskdetail, name='taskdetail'),
path('taskpage/<int:task_id>/subtask1page/<int:subtask1_id>', views.subtask1detail, name='subtask1detail'),

path('taskpage/<int:task_id>/subtask1page/<int:subtask1_id>/property/<int:id>', views.property_improvement, name='property_improvement'),
path('taskpage/<int:task_id>/evaluationsubtask1/<int:subtask1_id>', views.subtask1_improvement, name='subtask1_improvement'),
path('taskpage/<int:task_id>/evaluationtask', views.task_improvement, name='task_improvement'),


path('',views.index, name='index'),

]
