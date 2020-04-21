##TAREA: Programa Librería

Debes crear una aplicación dinámica en python flask con las siguientes características:  
**-** La aplicación nos va a permitir mostrar información de libros. Esa información está guardada en el fichero books.json.  
**-** La página principal debe mostrar una página donde ponga vuestro nombre, un título con la palabra "Biblioteca" y una lista de enlaces donde se vean los nombres de todos los libros y que nos lleve a una ruta del tipo /libro/<isbn>. Es decir si el libro 1 tienes ISBN 1933988673 el enlace nos llevara a la ruta /libro/1933988673.  
**-** Página detalle del libro. La ruta será /libro/<isbn>, que mostrará un título con el nombre del libro, una imagen del libro (campo thumbnailUrl) y la siguiente información del libro: Número de páginas, descripción, autores y categorías.  
**>** Si el ISBN no existe se devolverá un error 404.  
**>** Si el valor del campo status es igual a MEAP mostraremos un mensaje que diga "ESTE LIBRO NO SE HA PUBLICADO" (usar un if dentro de la plantilla).  

**Posible mejora (no es obligatorio, pero estaría muy bien que lo hagáis)**  
**-** Cuando se muestra el detalle de un libro y se muestran las categorías, estás son un enlace a la ruta /categoria/<categoria>. Por ejemplo, si el primer libro tiene una categoría  Mobile, al pulsar sobre el enlace nos lleva a la página /categoria/Mobile  
**-** Libros por categoría: Esta página está en la ruta /categoria/<categoria>: Es muy similar a la página principal, pero sólo muestra la los libros de esa ccategoría. Además debe a aprecer un título con la categoría.  

##Despliegue en heroku

Debes guardar la aplicación en un repositorio de GitHub para desplegarla posteriormente en Heroku.  
**¿Qué debes entregar?**  
**1.** La url del repositorio github donde has desarrollado el programa. Recuerda que debes hacer el programa poco a poco y que los cambios lo tienes que ir guardando con distintos commits.  
**2.** Debes entregar la URL de la aplicación funcionando en heroku.  
**3.** Entrega capturas de pantallas y explica el proceso para modificar la aplicación en desarrollo, probar la aplicación en desarrollo y volver a desplegar en heroku.  
**4.** Produce un error en la aplicación y muestra los logs de heroku donde se ve el error.
