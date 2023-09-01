from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm, AcademicDataForm, JobForm, About_MeForm, CoursesForm
from .models import Profile, Academic_Data, Job, About_Me, Courses
from django.contrib.auth.models import User

def index(request):
    context = {

    }

    return render(request, 'index.html', context)


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario creado: {username}')
            return redirect(to='profile')

        return render(request, self.template_name, {'form': form})
    

@login_required
def profile(request):
    #elementos comunes para todas las vistas
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = About_Me.objects.get(user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elementos para esta vista
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, 'Su perfil ha sido actualizado')
            return redirect(to='profile')
        
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 
                                            'profile_form': profile_form, 
                                            'datos_personales': datos_personales, 
                                            'academic_data': academic_data, 
                                            'courses': courses,
                                            'jobs': jobs, 
                                            'about_me': about_me})


@login_required
def create_academic_data(request):
    #elementos comunes para todas las vistas
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elementos para esta vista
    if request.method == 'POST':
        academic_form = AcademicDataForm(request.POST)
        if academic_form.is_valid():
            academic_form.save(user=request.user)
            return redirect('academic')
    else:
        academic_form = AcademicDataForm()
    
    return render(request, 'academic.html', {'datos_personales': datos_personales, 
                                             'academic_data': academic_data, 
                                             'jobs': jobs, 
                                             'about_me': about_me, 
                                             'courses': courses,
                                             'academic_form': academic_form})


@login_required
def update_academic_data(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elemento solo para esta vista:
    update_academic_data = get_object_or_404(Academic_Data, id=id)
    if request.method == 'POST':
        academic_form = AcademicDataForm(request.POST, instance=update_academic_data)
        if academic_form.is_valid():
            academic_form.save(user=request.user)
            return redirect('academic')
    else:
        academic_form = AcademicDataForm(instance=update_academic_data)
    return render(request, 'academic.html', {'datos_personales': datos_personales, 
                                             'academic_data': academic_data, 
                                             'jobs': jobs, 'about_me': about_me, 
                                             'courses': courses,
                                             'academic_form': academic_form, 
                                             'update_academic_data': update_academic_data,})


@login_required
def delete_academic_data(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elemento solo para esta vista:
    delete_academic_data = get_object_or_404(Academic_Data, id=id)
    if request.method == 'POST':
        delete_academic_data.delete()
        return redirect('profile')
    return render(request, 'delete-academic.html', {'datos_personales': datos_personales, 
                                                    'academic_data': academic_data, 
                                                    'jobs': jobs, 
                                                    'about_me': about_me, 
                                                    'courses': courses,
                                                    'delete_academic_data': delete_academic_data,})


@login_required
def add_job(request):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elemento solo para esta vista:
    if request.method == 'POST':
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job_form.save(user=request.user)
            return redirect('add_job')
    else:
        job_form = JobForm()

    return render(request, 'jobs.html', {'datos_personales': datos_personales, 
                                         'academic_data': academic_data, 
                                         'jobs': jobs, 
                                         'about_me': about_me, 
                                         'courses': courses,
                                         'job_form': job_form})



@login_required
def update_job(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elemento solo para esta vista:
    update_job_data = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        job_form = JobForm(request.POST, instance=update_job_data)
        if job_form.is_valid():
            job_form.save(user=request.user)
            return redirect('add_job')
    else:
        job_form = JobForm(instance=update_job_data)

    return render(request, 'jobs.html', {'datos_personales': datos_personales, 
                                         'academic_data': academic_data, 
                                         'jobs': jobs, 
                                         'about_me': about_me, 
                                         'courses': courses,
                                         'job_form': job_form,
                                         'update_job_data': update_job_data})



@login_required
def delete_job(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elemento solo para esta vista:
    delete_job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        delete_job.delete()
        return redirect('profile')

    return render(request, 'delete_job.html', {'datos_personales': datos_personales, 
                                         'academic_data': academic_data, 
                                         'jobs': jobs, 
                                         'about_me': about_me,
                                         'courses': courses,
                                         'delete_job': delete_job,})



@login_required
def about_me(request):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')

    #elemento solo para esta vista:
    if request.method == 'POST':
        if about_me:
            about_me_form = About_MeForm(request.POST, instance=about_me)
        else:
            about_me_form = About_MeForm(request.POST)
        
        if about_me_form.is_valid():
            instance = about_me_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('about_me')
    else:
        if about_me:
            about_me_form = About_MeForm(instance=about_me)
        else:
            about_me_form = About_MeForm()

    return render(request, 'about_me.html', {'datos_personales': datos_personales, 
                                             'academic_data': academic_data, 
                                             'jobs': jobs, 
                                             'about_me': about_me, 
                                             'courses': courses,
                                             'about_me_form': about_me_form})


@login_required
def add_course(request):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')
    
    #elemento solo para esta vista:
    if request.method == 'POST':
        course_form = CoursesForm(request.POST)
        if course_form.is_valid():
            course_form.save(user=request.user)
            return redirect('add_course')
    else:
        course_form = CoursesForm()

    return render(request, 'courses.html', {'datos_personales': datos_personales,
                                             'academic_data': academic_data,
                                             'jobs': jobs,
                                             'about_me': about_me,
                                             'courses': courses,
                                             'course_form': course_form})


@login_required
def course_update(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')

    #elemento solo para esta vista:
    update_course = get_object_or_404(Courses, id=id)
    if request.method == 'POST':
        course_form = CoursesForm(request.POST, instance=update_course)
        if course_form.is_valid():
            course_form.save(user=request.user)
            return redirect('add_course')
    else:
        course_form = CoursesForm(instance=update_course)

    return render(request, 'courses.html', {'datos_personales': datos_personales,
                                             'academic_data': academic_data,
                                             'jobs': jobs,
                                             'about_me': about_me,
                                             'courses': courses,
                                             'update_course': update_course,
                                             'course_form': course_form})


@login_required
def course_delete(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    jobs = Job.objects.filter(user=request.user).order_by('-trabaja_actualmente', '-year_fin', '-month_fin', 'created_at')
    about_me = get_object_or_404(About_Me, user=request.user)
    courses = Courses.objects.filter(user=request.user).order_by('-year_egreso')

    #elemento solo para esta vista:
    delete_course = get_object_or_404(Courses, id=id)
    if request.method == 'POST':
        delete_course.delete()
        return redirect('add_course')

    return render(request, 'delete_course.html', {'datos_personales': datos_personales,
                                             'academic_data': academic_data,
                                             'jobs': jobs,
                                             'about_me': about_me,
                                             'courses': courses,
                                             'delete_course': delete_course,})