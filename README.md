# Motor_busqueda_ETL

### 1. Introducción

La presente guía tiene como fin servir de instructivo para los usuarios del sistema motor de búsqueda basado en tecnicas de web scraping desarrollado para la comunidad académica de la universidad Distrital. El manual contara con dos instructivos, uno para usuarios finales quienes son los que simplemente usan la aplicación, y un instructivo para usuarios desarrolladores los cuales podrán experimentar con el código del proyecto.

El manual detallara varios aspectos técnicos como por ejemplo requerimientos, pasos de instalación y configuraciones, por otro algunos de los procesos del manual serán explicados de manera ilustrativa para un fácil entendimiento por parte del usuario, la guía tendrá un enfoque practico y será desarrollada por medio de ejemplos sencillos que el usuario puede realizar y comprobar.

### 2. Objetivos

Definir un manual de usuario a manera ilustrativa el cual pueda instruir al usuario de todos los procesos del sistema motor de búsqueda 

### 2. Objetivos específicos

- Definir un manual para el usuario final del sistema motor de búsqueda de horarios y espacios académicos el cual explique todos los procesos de usuario relacionados.
- Definir un manual para el usuario desarrollador, este estará enfocado en todos los procesos relacionados a la configuración del ambiente de desarrollo con el fin de que el programador pueda experimentar con código del proyecto.


### 3. MANUAL PARA USUARIOS

El motor de búsqueda de horarios y espacios académicos tiene una aplicación web que servirá como interfaz para todos aquellos usuarios que quieran hacer consultas online de manera rápida y fácil, la aplicación web estará disponible en internet, es decir que estará disponible ante cualquier usuario en internet.

para acceder a la aplicación se debe hacer desde el siguiente enlace: https://horarios-ud.web.app ,los datos pertenecientes a cada columna son de vital importancia para el proceso de consulta, cada columna tiene un significado dentro del proceso de inscribir espacios académicos en el estudiante, a continuación, se definirá un diccionario de datos con el fin de brindar información detallada de cada columna para la consulta.

#### 3.1 Elementos de la interfaz de usuario

Ahora que se tiene un entendimiento de los datos y de la funcionalidad básica del aplicativo, se definen los componentes de la interfaz de usuario previo a los procesos de consulta, los elementos de interfaz de usuario tienen funcionalidades puntuales, están definidas de la siguiente manera.

**Figura 2.** Elementos interfaz de usuario - parte superior izquierda


![Figura_2](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_2.PNG)

De los elementos de la anterior imagen se puede destacar la caja de búsqueda y los filtros, el campo para buscar realiza una búsqueda en tiempo real sobre toda la base de datos, se puede buscar cualquier dato de cualquier columna o inclusive buscar cualquier palabra clave de cualquier columna y los resultados de la consulta se podrán ver reflejados en cuestión de milisegundos, por otro lado, los filtros hacen la misma consulta, pero solo dentro de la columna del filtro.

**Figura 3.** Elementos interfaz de usuario - parte inferior izquierda

![Figura_3](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_3.PNG)

En el apartado inferior izquierdo de la interfaz de la aplicación encontrara un recuento del total de información que hay disponible para la consulta, cada registro de la base de datos este compuesto de toda la información del espacio académico en cuestión, además cada registro en base de datos corresponde a una hora de clase, dicho esto es posible saber cuantas horas de clase semanal tiene asignado un docente o un espacio académico.

**Figura 4.** Elementos interfaz de usuario - parte inferior derecha

![Figura_4](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_4.PNG)

Ahora al ubicarse en la parte inferior derecha de la interfaz de usuario encontrara un panel con varios botones, estos definen el desplazamiento sobre la información, asuma que toda la base de datos es un gran libro con mucha información la cual es imposible mostrarla en una sola interfaz de usuario, lo que se hace es lo mismo que con un libro dividir toda la información consecutivamente por páginas, es decir que podrá desplazarse sobre toda la información de la base de datos por paginas cada una con 10 registros. 

**Figura 5.** Elementos interfaz de usuario – cuerpo del motor de búsqueda

![Figura_5](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_5.PNG)

Finalmente el cuerpo del motor de búsqueda lo puede asumir como una hoja de cálculo de Excel o como un libro online donde se puede desplazar por la información en las diferentes páginas, observe en la figura 5 que en los nombres de columna al lado hay un botón con un icono de dos flechas muy pequeñas, este botón sirve para ordenar la base de datos por columna, como puede observar en la imagen anterior al dar click en la columna asignatura los datos pueden quedar en orden alfabético de manera ascendente o descendente.

### 3.2 Consultas sobre la aplicación

Ahora que se tiene una idea del funcionamiento de la aplicación y su interfaz realiza rconsultas sobre la aplicación es un proceso bastante sencillo, dentro de la aplicación hay do stipos de consulta, la búsqueda general que hace una búsqueda sobre toda la base de datos y los filtros de búsqueda los cuales solo hacen consultas sobre columnas especificas de la base de datos, a continuación, observe un primer ejemplo acerca de una consulta en general.

**Figura 6.** Consulta general en el motor de búsqueda

![Figura_6](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_6.PNG)

Observe que en la figura anterior la búsqueda se dio en toda la base de datos y como resultado se pueden observar 540 horas de clase semanales para el espacio académico de calculo diferencial impartido por varias carreras en varias facultades, si desea hacer consultas basadas en palabras clave, el motor de búsqueda también permite realizar este tipo de consultas, a continuación, observe los resultados de búsqueda para la palabra datos.

**Figura 7.** Consulta por palabra clave en el motor de búsqueda

![Figura_7](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_7.PNG)

Los resultados de la búsqueda anterior son los resultados de la búsqueda de la palabra datos en todas las columnas de la base de datos como puede ver en la figura 7 la búsqueda encontró resultados de esa palabra tanto en la columna proyecto curricular como en la columna asignatura, este tipo de búsquedas son efectivas para palabras clave poco habituales, pero en palabras muy usadas o conectores se asumen como ambigüedades dando una consulta poco especifica.

### 3.3 Subconsultas

Existen situaciones en el contexto de los espacios académicos donde se requiere filtrar información sobre varios criterios de consulta, como por ejemplo saber que días se dicta un determinado espacio académico únicamente en un proyecto curricular o mejor aun consultar sobre un día en especifico dentro de un proyecto curricular.
