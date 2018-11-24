from django import forms # importacion de la libreria forms
#from .models import Mascota
#Creamos las tuplas de datos a utilizar en las diferentes selecciones

#Tipos de usuarios para crear
perfiles=(
    
    ('Usuario','Usuario'),
)

#Regiones a usar
regiones=(
    ('Region Metropolitana','Region Metropolitana'),
)

#Ciudades a usar
ciudades=(
    ('Santiago','Santiago'),
    ('Providencia','Providencia'),
    ('Puente Alto','Puente Alto'),
)

#Tipos de vivienda disponibles
vivienda=(
    ('Casa con Patio Grande','Casa con Patio Grande'),
    ('Casa con Patio Pequeno','Casa con Patio Pequeno'),
    ('Casa sin Patio','Casa sin Patio'),
    ('Departamento','Departamento'),

)

#Estado de la mascota que sera ingresada al sistema que por defecto sera rescatado
estadoM=(
    ('Rescatado','Rescatado'),
    ('Disponible','Disponible'),
    ('Adoptado','Adoptado'),
)

#Raza de los perros que por momento solo estan disponibles estas jaja
raza=(
    ('Akita','Akita'),
    ('Basset Hound','Basset Hound'),
    ('Golden Retriever','Golden Retriever'),
    ('Kiltro','Kiltro'),
)

#La estructura de los datos que seran ingresados para registrar clientes y el orden de estos, maxima cantidad de caracteres, son requeridos para enviar la informacion
class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),max_length=20,label="Nombre de Usuario",required=True)
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña",required=True)
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo Electronico",required=True) #Nos pedira que sea ingresado en formato correo ej: "cualquier cosa"@"4 letras maximo"."3 letras maximo"
    nombreCliente=forms.CharField(widget=forms.TextInput(),max_length=20,label="Nombre Completo",required=True)
    fechaCliente=forms.DateField(widget=forms.SelectDateWidget(years=range(1900,2001)),label="Fecha de Nacimiento",required=True) # SelectDateWidget nos permitira elegir la fecha en un calendario
    telefonoCliente=forms.CharField(widget=forms.TextInput(),max_length=8,label="Telefono de Contacto +569",required=True)
    regionCliente=forms.ChoiceField(choices=regiones,label="Region",required=True) # ChoiceField --> choices nos permitira cargar las tuplas anteriormente creadas y las mostrara en combobox para elegir ne esete caso region
    ciudadCliente=forms.ChoiceField(choices=ciudades,label="Ciudad",required=True) # Aca muestra las ciudades
    viviendaCliente=forms.ChoiceField(choices=vivienda,label="Tipo Vivienda",required=True)# Aca los tipos de vivienda
    perfil=forms.ChoiceField(choices=perfiles)

#form para el html login
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario",required=True) #Campo para ingreasr el nombre de usuario 
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña",required=True) # Campo de password

#form para ingresar una nueva mascota a la base de datos
class AgregarMascota(forms.Form):
    fotoMascota=forms.ImageField(label="Foto Mascota",required=True) #imagefield nos permitira cargar una imagen desde el computador
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota",max_length=20,required=True)
    razaMascota=forms.ChoiceField(choices=raza,label="Raza Mascota",required=True) # nuevamente eleccion en un combobox
    descripcionMascota=forms.CharField(widget=forms.Textarea(),max_length=250,label="Descripcion Mascota",required=True)
    estadoMascota=forms.ChoiceField(choices=estadoM,label="Estado Mascota",required=True) #nuevamente eleccion en un combobox
#Intento fallido de subir la imagen buscar mas opciones
#class AgregarMascota(forms.ModelForm):
#    class Meta:
 #       model = Mascota
  #      fields = ['fotoMascota', 'nombreMascota', 'razaMascota','descripcionMascota','estadoMascota']
    
    

#form para enviar un correo 
class Contacto(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(),required=True)
    email=forms.EmailField(widget=forms.TextInput())
    mensaje=forms.CharField(widget=forms.Textarea(),required=True,max_length=200) # textarea hace quye el campo sea mas grande 

#form para recuperar contrasena
class Recuperrar(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")

#form para nueva contrasena
class NuevaPass(forms.Form):
    nueva=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña")
    repite_nueva=forms.CharField(widget=forms.PasswordInput(),label="Repita Contraseña")
