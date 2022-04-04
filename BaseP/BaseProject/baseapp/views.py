from django.contrib.auth.models import User
from django.shortcuts import render
from baseapp.models import Tasks, SubTasks1, Properties, Profile
from baseapp.forms import NewTaskForm, NewSubTask1Form, New_Property_Form, Question_Form
from django.contrib.auth.decorators import permission_required

def newtask(request, task_id):
    form = NewTaskForm(initial={'task_id': 'task_id','task_creator':'user.get_username'})
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.instance.task_creator = request.user
            newtask_id = task_id+1
            latest_task_id = Tasks.objects.latest('task_id').task_id
            max = latest_task_id
            while (task_id < max):
                  Tasks.objects.filter(task_id=max).update(task_id = max+1)
                  max = max-1
            form.instance.task_id = newtask_id
            form.save(commit=True)
            return list(request)
    else:
        pass
    return render(request,'baseapp/newtask.html',{'form':form})

@permission_required('baseapp.change_tasks', raise_exception=True)
def task_improvement(request, task_id):
    task = Tasks.objects.get(task_id=task_id)
    user_creator_profile = Profile.objects.get(user=task.task_creator)
    form = NewTaskForm(instance=task)
    if request.method == 'POST':
        form = NewTaskForm(request.POST, instance=task)
        print("با تشکر از بروزرسانی و ارزیابی وظیفه ")
#        editor =
 #       print(f"creator is:{creator}")
  #      print(f"previous user point is:{user_creator_profile.user_point}")
        if form.is_valid():
          repetition_check = request.POST.get('repetition_check')
          print("repetition_check")
          if repetition_check == "repeated":
         #     print(f"{request.user} آیا از تکراری بودن تجربه ثبت شده مطمئن هستید؟ "
         #                         f"  پس از تایید شما، تجربه ثبت شده حذف خواهد شد ")
        #      print("thank you for your paticipation but your experience had been submitted by some one else")
              repeted_task_score = 0.5
              user_creator_profile.user_score += repeted_task_score
              print(f"user_creator_profile is : {user_creator_profile}")
           #   print(f"property score is : {property1.property_score}")
              print(f"updated user point is:{user_creator_profile.user_point}")
              user_creator_profile.number_of_repeated_tasks += 1
              user_creator_profile.save()
              task.delete()
              #return HttpResponse(f"Dear {request.user} thank you for your paticipation but your experience had been submitted by some one else")

          else:

              form.save(commit=True)
              task.amendment_condition = True
              task.save()
              user_creator_profile.user_score += task.task_score
              user_creator_profile.number_of_new_tasks += 1
              print(f"user_creator_profile is : {user_creator_profile}")
              print(f"property score is : {task.task_score}")
              print(f"updated user point is:{user_creator_profile.user_point}")
              task.save()
              user_creator_profile.save()
          return list(request)
    else:
        print("اطلاعات وارد شده صحیح نیست")
    return render(request,'baseapp/newtask.html',{'form':form})


def newsubtask1(request, task_id, subtask1_id):
    task = Tasks.objects.get(task_id = task_id)
    newsubtask1_id = subtask1_id+1
    form = NewSubTask1Form(initial={'related_task': 'task','subtask1_id':'newsubtask1_id'})
    if request.method == 'POST':
        form = NewSubTask1Form(request.POST)
        print("با تشکر"),
        if form.is_valid():
            subtask1_list = SubTasks1.objects.order_by('subtask1_id')
            try:
                max_subtask1_id = SubTasks1.objects.latest('subtask1_id').subtask1_id
            except:
                max_subtask1_id = 1
            finally:
                max = max_subtask1_id

            while (max > subtask1_id):
                            SubTasks1.objects.filter(subtask1_id=max).update(subtask1_id = max+1)
                            max = max-1
            form.instance.related_task = Tasks.objects.get(
                task_id=task_id)
            form.instance.subtask1_id = newsubtask1_id
            form.instance.subtask1_creator = request.user
#
            form.instance.amendment_condition = False
#
            form.save(commit=True)
            return taskdetail(request, id=task_id)
    else:
        print("اطلاعات صحیح نیست")
    return render(request,'baseapp/newsubtaskform.html',{'form':form})

@permission_required('baseapp.change_subtasks1', raise_exception=True)
def subtask1_improvement(request, task_id, subtask1_id):
    subtask1 = SubTasks1.objects.get(subtask1_id=subtask1_id)
    user_creator_profile = Profile.objects.get(user=subtask1.subtask1_creator)
    form = NewSubTask1Form(instance=subtask1)
    if request.method == 'POST':
        form = NewSubTask1Form(request.POST, instance=subtask1)
        print("با تشکر از بروزرسانی و ارزیابی زیروظیفه گروه1")

#        editor =
 #       print(f"creator is:{creator}")
  #      print(f"previous user point is:{user_creator_profile.user_point}")

        if form.is_valid():
          repetition_check = request.POST.get('repetition_check')
          print("repetition_check")
          if repetition_check == "repeated":

         #     print(f"{request.user} آیا از تکراری بودن تجربه ثبت شده مطمئن هستید؟ "
         #                         f"  پس از تایید شما، تجربه ثبت شده حذف خواهد شد ")

        #      print("thank you for your paticipation but your experience had been submitted by some one else")
              repeted_subtask1_score = 0.5
              user_creator_profile.user_score += repeted_subtask1_score
              print(f"user_creator_profile is : {user_creator_profile}")
           #   print(f"property score is : {property1.property_score}")
              print(f"updated user point is:{user_creator_profile.user_point}")
              user_creator_profile.number_of_repeated_subtask1s += 1
              user_creator_profile.save()
              subtask1.delete()
              #return HttpResponse(f"Dear {request.user} thank you for your paticipation but your experience had been submitted by some one else")

          else:

              form.save(commit=True)

              user_creator_profile.user_score += subtask1.property_score
              user_creator_profile.number_of_new_subtask1s += 1
              subtask1.amendment_condition = True
              subtask1.save()
              print(f"user_creator_profile is : {user_creator_profile}")
              print(f"property score is : {subtask1.property_score}")
              print(f"updated user point is:{user_creator_profile.user_point}")
              user_creator_profile.save()
              print(subtask1.amendment_condition)
          return taskdetail(request, id=task_id)
    else:
        print("اطلاعات وارد شده صحیح نیست")
    return render(request,'baseapp/newsubtaskform.html',{'form':form})



def task_property(request, task_id, subtask1_id):

    current_user = request.user

    subtask1 = SubTasks1.objects.get(subtask1_id=subtask1_id)
    form = New_Property_Form(initial={'related_subtask1':'subtask1'})
    if request.method == 'POST':
        form = New_Property_Form(request.POST)
        print("با تشکر")
        if form.is_valid():
            form.instance.related_subtask1 = SubTasks1.objects.get(
              subtask1_id = subtask1_id)

            form.instance.experience_creator = current_user

            subtask1.number_of_submitted_experiences += 1

            form.save(commit=True)
            subtask1.save()


            return subtask1detail(request, task_id=task_id, subtask1_id=subtask1_id)
    else:
        print("اطلاعات وارد شده صحیح نیست")
    return render(request,'baseapp/new_properties.html',{'form':form})

def subtask1_questions(request, task_id, subtask1_id):
    subtask1 = SubTasks1.objects.get(subtask1_id=subtask1_id)
    form = Question_Form(initial={'related_subtask1':'subtask1'})
    if request.method == 'POST':
        form = Question_Form(request.POST)
        print("با تشکر")
        if form.is_valid():
            form.instance.related_subtask1 = SubTasks1.objects.get(
              subtask1_id = subtask1_id)
            form.instance.question_creator = request.user
            form.save(commit=True)
            return subtask1detail(request, task_id=task_id, subtask1_id=subtask1_id)
    else:
        print("اطلاعات وارد شده صحیح نیست")
    return render(request,'baseapp/new_questions.html',{'form':form})



@permission_required('baseapp.change_properties', raise_exception=True)
def property_improvement(request, task_id, subtask1_id,id):
    property1 = Properties.objects.get(id=id)
    subtask1 = SubTasks1.objects.get(subtask1_id=subtask1_id)
    user_creator_profile = Profile.objects.get(user=property1.experience_creator)
    form = New_Property_Form(instance=property1)
    if request.method == 'POST':
        form = New_Property_Form(request.POST, instance=property1)
        print("با تشکر از بروزرسانی و ارزیابی تجربه")
 #       creator = property1.experience_creator
#        editor =
 #       print(f"creator is:{creator}")
  #      print(f"previous user point is:{user_creator_profile.user_point}")

        if form.is_valid():
          repetition_check = request.POST.get('repetition_check')
   #       print("repetition_check")
          if repetition_check == "repeated":
        #      return HttpResponse(f"{request.user} آیا از تکراری بودن تجربه ثبت شده مطمئن هستید؟ "
        #                          f"  پس از تایید شما، تجربه ثبت شده حذف خواهد شد ")
              print("thank you for your paticipation but your experience had been submitted by some one else")
              repeted_experience_score = 0.5
              user_creator_profile.user_score += repeted_experience_score
              print(f"user_creator_profile is : {user_creator_profile}")
              print(f"property score is : {property1.property_score}")
              print(f"updated user point is:{user_creator_profile.user_point}")
              user_creator_profile.number_of_repeated_experiences += 1
              subtask1.number_of_submitted_experiences -= 1
              subtask1.save()
              user_creator_profile.save()
              property1.delete()
              #return HttpResponse(f"Dear {request.user} thank you for your paticipation but your experience had been submitted by some one else")

          else:

              form.save(commit=True)

              user_creator_profile.user_score += property1.property_score
              user_creator_profile.number_of_new_experiences += 1
              subtask1.number_of_verified_experiences += 1
              subtask1.number_of_submitted_experiences -= 1
              property1.amendment_condition = True          #repeatetive evaluation is not allowed
              print(f"user_creator_profile is : {user_creator_profile}")
              print(f"property score is : {property1.property_score}")
              print(f"updated user point is:{user_creator_profile.user_point}")
              property1.save()       #owing to amended
              user_creator_profile.save()
              subtask1.save()

          return subtask1detail(request, task_id=task_id, subtask1_id=subtask1_id)
    else:
        print("اطلاعات وارد شده صحیح نیست")
    return render(request,'baseapp/new_properties.html',{'form':form})


#@permission_required('tasks.can_view', raise_exception=True)
def list(request):
    tasks_list = Tasks.objects.order_by('task_id')
#    tasks_dict = {'tasks':tasks_list}
    subtask1_list = SubTasks1.objects.order_by('id')
#    subtask1_dict = {'subtask1s':subtask1_list}
    properties_list = Properties.objects.order_by('id')
#    property_dict = {'properties':properties_list}
    #return task
    return render (request,'baseapp/tasks.html',context={'tasks':tasks_list,'properties':properties_list, 'subtasks1':subtask1_list})

def taskdetail(request,id):
    task = Tasks.objects.get(task_id = id)
    subtask1_list = SubTasks1.objects.order_by('subtask1_id')
    try:    #if there is no any task yet
        max_subtask1_id = SubTasks1.objects.latest('subtask1_id').subtask1_id

    except:
        max_subtask1_id = 1
    finally:
        max_subtask1_id += 1

    return render(request, 'baseapp/taskpage.html', context = {'task':task,'subtasks1':subtask1_list, 'max_subtask1_id':max_subtask1_id})

def subtask1detail(request,task_id,subtask1_id):
    task = Tasks.objects.get(task_id = task_id)

    subtask1 = SubTasks1.objects.get(subtask1_id = subtask1_id)

    #try:
    properties = Properties.objects.order_by('id')

    #except Properties.DoesNotExist:
#        from django.http import HttpResponse
#        return HttpResponse(" تاکنون تجربه ای مرتبط با این وظیفه ثبت نشده است ")
    #    return render(request, 'baseapp/subtask1page.html', context={'subtask1':subtask1,'task':task,'property':None})


    return render(request, 'baseapp/subtask1page.html', context={'subtask1':subtask1,'task':task,'properties':properties})
'''

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'baseapp/registration.html',{'user_form':user_form})
'''
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.db.models import Max
@login_required
def index(request):
    try:
        current_user = Profile.objects.get(user=request.user)
   #     user_dict = {"current_user": current_user}
    except Profile.DoesNotExist:
        profile = None
        current_user = ""

    max_score = Profile.objects.aggregate(Max('user_score'))['user_score__max']
  #  score_dict = {"max_score":max_score}
    print(f"max score is {max_score}")
    context = { "current_user": current_user, "max_score":max_score }
    return render(request, "index.html", context)

'''
    #accounts
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.forms import User

from django.shortcuts import render, redirect
from baseapp.forms import SignUpForm

#sign up
def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('../login/')
    return render(request, 'accounts/signup.html', {'form': form})

#logging out
def logout_request(request):
    #logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('../login/')

#login

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request,'baseapp/tasks.html',{'username':username})
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("SSAADDDD")


from django.contrib import messages
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                #send tag to personal profile
                return render(request,'baseapp/tasks.html',{'username':username})
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})
'''