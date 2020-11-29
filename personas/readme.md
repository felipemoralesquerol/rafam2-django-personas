python manage.py shell
Lectura de consultas SQL ejecutadas

>>> from django.db import connection
>>> connection.queries

Importación de modelos
from data.models import Persona, Direccion

Mostrar todos los datos
Persona.objects.all()

Muestra persona via pk
Persona.objects.get(pk=1)

Filtrar algunas personas
Persona.objects.filter(nombre = 'Felipe')

Mostrar ultimo query ejecutado
print(connection.queries[-1])

USO DE shell_plus
Requiere pip install django_extensions
Luego en INSTALLED_APP agregar django_extensions y listo!
python manage.py shell_plus --print-sql
