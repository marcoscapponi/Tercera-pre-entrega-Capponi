Pasos para compra:
Este proyecto consta de una pagina de indumentaria en la que el cliente debe ingresar datos necesarios para la empresa al realizar una compra.
La pagina web tiene una pagina de inicio que tiene tres paginas a tomar: prenda, datos personales y medios de pago. Es obligatorio ingresar a las tres paginas y cargar todos los daatos. Se puede acceder mediante una navbar o haciendo click en las imagenes que se aprecian en la pagina de inicio.
El proyecto consta de dos carpetas creadas con django, una carpeta principal que tiene de gran importancia los settings del proyecto, y una carpeta appentrega,
donde se han creado los forms de la pagina para que el usuario ingrese su compra, los modelos, las vistas necesarias para la pagina y las urls que conectan las vistas a la pagina web. 
Dentro de la carpeta appentrega hay una carpeta templates que contiene una carpeta con todos los templates del proyecto. En estos templates tendras el template base y luego los demas qeu heredan la estructura de este.
Tambien tenemos una carpeta static con toda la formacion estetica de los templates, tenemos los archivos css y jss para el modelado de los templates.
Con estas dos carpetas principales, contamos con una base de datos, donde se almacenan todas las compras realizadas por los usuarios.
Y por ultimo tenemos el archivo manage.py que se crea automaticamente al crear un proyecto django. Este archivo es de suma importancia ya que es el punto de entrada para varias tareas de gestion del proyecto, establece la 
configuracion del entorno y tambien permite ejecutar una variedad de comandos de administracion de django.
