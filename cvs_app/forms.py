from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import Profile, Academic_Data, Job, About_Me, Courses

#este modelo de formulario es para crear un nuevo usuairo
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control', 'autocomplete': "off"}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control', 'autocomplete': "off"}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control', 'autocomplete': "off"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'autocomplete': "off"}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'autocomplete': "off"}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'autocomplete': "off"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


#este modelo de formulario es para editar los campos auth que vienen de usuarios de django
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    email = forms.EmailField(required=True,  widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


#este modelo de formulario es para editar los campos de datos personales que no vienen de usuarios de django
class UpdateProfileForm(forms.ModelForm):
    dni = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'DNI', 'class': 'form-control', 'autocomplete': "off"}))
    prefijo_cuil = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'XX', 'class': 'form-control', 'autocomplete': "off"}))
    sufijo_cuil = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'X', 'class': 'form-control', 'autocomplete': "off"}))
    cod_area = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Código de área', 'class': 'form-control', 'autocomplete': "off"}))
    telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class': 'form-control', 'autocomplete': "off"}))
    domicilio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Domicilio','class': 'form-control', 'autocomplete': "off"}))
    localidad = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Localidad','class': 'form-control', 'autocomplete': "off"}))
    provincia = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Provincia','class': 'form-control', 'autocomplete': "off"}))
    nacionalidad = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nacionalidad','class': 'form-control', 'autocomplete': "off"}))
    genero = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Género','class': 'form-control', 'autocomplete': "off"}))
    day = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'DD', 'class': 'form-control', 'autocomplete': "off"}))
    month = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'form-control', 'autocomplete': "off"}))
    year = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control', 'autocomplete': "off"}))
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    estado_civil = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Estado civil','class': 'form-control', 'autocomplete': "off"}))
    imprime_estado_civil = forms.BooleanField(label='Incluir en cv', required=False,)
    cantidad_hijos = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Hijos','class': 'form-control', 'autocomplete': "off"}))
    imprime_cantidad_hijos = forms.BooleanField(label='Incluir en cv', required=False,)


    class Meta:
        model = Profile
        fields = ['dni', 'prefijo_cuil', 'sufijo_cuil', 'cod_area', 'telefono', 'domicilio', 'localidad', 'provincia', 'nacionalidad', 'genero', 'day', 'month', 'year', 'foto', 'estado_civil', 'imprime_estado_civil', 'cantidad_hijos', 'imprime_cantidad_hijos']



class AcademicDataForm(forms.ModelForm):
    escuela = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Institución/Universidad', 'class': 'form-control', 'autocomplete': "off"}))
    titulo = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Titulo obtenido', 'class': 'form-control', 'autocomplete': "off"}))
    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción', 'class': 'form-control', 'autocomplete': "off"}))
    year_inicio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA','class': 'form-control', 'autocomplete': "off"}))
    year_fin = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control', 'autocomplete': "off"}))


    class Meta:
        model = Academic_Data
        fields = ['nivel', 'estado', 'escuela', 'titulo', 'descripcion', 'year_inicio', 'year_fin']

    def save(self, user, commit=True):
        instance = super(AcademicDataForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance
    

class JobForm(forms.ModelForm):
    empresa = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': '¿Para quién o donde trabajabas?', 'class': 'form-control', 'autocomplete': "off"}))
    puesto = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Actividad desempeñada', 'class': 'form-control', 'autocomplete': "off"}))
    month_inicio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'form-control', 'autocomplete': "off"}))
    year_inicio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control', 'autocomplete': "off"}))
    month_fin = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'form-control', 'autocomplete': "off"}))
    year_fin = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control', 'autocomplete': "off"}))
    referencia_nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre y apellido', 'class': 'form-control', 'autocomplete': "off"}))
    referencia_puesto = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Puesto', 'class': 'form-control', 'autocomplete': "off"}))
    referencia_cod_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Cod. área (sin cero)', 'class': 'form-control', 'autocomplete': "off"}))
    referencia_telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Teléfono (sin 15)', 'class': 'form-control', 'autocomplete': "off"}))
    trabaja_actualmente = forms.BooleanField(label='Trabaja actualmente?', required=False,)

    class Meta:
        model = Job
        fields = ['empresa', 'puesto', 'month_inicio', 'year_inicio', 'month_fin', 'year_fin', 'referencia_nombre', 'referencia_puesto', 'referencia_cod_area', 'referencia_telefono', 'trabaja_actualmente']
    
    def save(self, user, commit=True):
        instance = super(JobForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance
    

class About_MeForm(forms.ModelForm):
    objetivo = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 7, 'placeholder': 'Redacte sus objetivos laborales', 'class': 'form-control', 'autocomplete': "off"}))
    objetivo_imp = forms.BooleanField(label='Incluir en cv', required=False,)
    aptitudes = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 7, 'placeholder': 'Redacte sus aptitudes', 'class': 'form-control', 'autocomplete': "off"}))
    aptitudes_imp = forms.BooleanField(label='Incluir en cv', required=False,)
    habilidades = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 7, 'placeholder': 'Redacte sus habilidades', 'class': 'form-control', 'autocomplete': "off"}))
    habilidades_imp = forms.BooleanField(label='Incluir en cv', required=False,)

    class Meta:
        model = About_Me
        fields = ['objetivo', 'objetivo_imp', 'aptitudes', 'aptitudes_imp', 'habilidades', 'habilidades_imp']



class CoursesForm(forms.ModelForm):
    nombre_curso = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre capacitación/certificación', 'class': 'form-control', 'autocomplete': "off"}))
    institucion = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '¿Donde lo realizaste?', 'class': 'form-control', 'autocomplete': "off"}))
    duracion = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Horas/Días/Meses/Años', 'class': 'form-control', 'autocomplete': "off"}))
    year_egreso = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control', 'autocomplete': "off"}))

    class Meta:
        model = Courses
        fields = ['nombre_curso', 'institucion', 'duracion', 'year_egreso']

    def save(self, user, commit=True):
        instance = super(CoursesForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance