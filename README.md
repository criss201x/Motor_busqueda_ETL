# Motor_busqueda_ETL

### 1. Introducción

La presente guía tiene como fin servir de instructivo para los usuarios del sistema motor de búsqueda basado en tecnicas de web scraping desarrollado para la comunidad académica de la universidad Distrital. El manual contara con dos instructivos, uno para usuarios finales quienes son los que simplemente usan la aplicación, y un instructivo para usuarios desarrolladores los cuales podrán experimentar con el código del proyecto.

El manual detallara varios aspectos técnicos como por ejemplo requerimientos, pasos de instalación y configuraciones, por otro algunos de los procesos del manual serán explicados de manera ilustrativa para unfácil entendimiento por parte del usuario, la guía tendrá un enfoque practico y será desarrollada por medio de ejemplos sencillos que el usuario puede realizar y comprobar.

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

**Figura 8.** Subconsultas en el motor de búsqueda

![Figura_8](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_8.PNG)

Con esta funcionalidad es posible acceder a toda la información de la base de datos en tan solo segundos, además también es posible agregar todos los filtros que sean necesarios para realizar una sub consulta

### 3.4 Aplicación en dispositivos móviles

La aplicación esta lejos de ser una aplicación móvil o una aplicación hibrida multiplataforma sin embargo al ser una aplicación web moderna esta es compatible con smartphone y tabletas, o cualquier dispositivo que cuente con un navegador web.

La vista de la aplicación en dispositivos móviles no es muy diferente a la de la aplicación en la computadora, la aplicación se ajusta a la resolución de pantalla, es decir que entre mas

reducida sea la resolución más contraídos se verán los elementos de la interfaz de usuario, a continuación, observe como se ve la aplicación en un teléfono con resolución 1920*1280

**Figura 9.** Interfaz del motor de búsqueda en dispositivos móviles

![Figura_9](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_9.PNG)

Solo se necesitó de la url de la aplicación para poderla ejecutar desde el teléfono móvil esto trae una ventaja frente a una aplicación nativa al no requerir de una instalación como es habitual en sistemas operativos móviles, por otro lado, en el móvil la aplicación solo funcionara si el teléfono cuenta con una conexión a internet.

### 4. MANUAL PARA DESARROLLADORES

El presente apartado pretende servir como guía para desarrolladores interesados en experimentar con el código del proyecto inicialmente se sugiere tener en cuenta que son necesarios conocimientos en programación orientada a objetos, conocimientos en el lenguaje de programación Python, conocimientos en Javascript y conocimientos en bases de datos NoSQL para un adecuado entendimiento de las practicas.

### 4.1 Requisitos

El usuario desarrollador ademas de contar con un equipo y una conexiona internet debe tener las siguientes herramientas instaladas para poder experimentar con el código del proyecto.

- Python 3.6 o superior
- Visual Studio Code
- Node JS versión lts
- NPM versión lts
- Anaconda Enviroment
- Jupyter lab

A continuación, se explicará la configuración de herramientas recomendada para el proyecto con el fin de definir un ambiente de desarrollo idóneo para trabajar en sincronía.

### 4.2 Instalación Python 3 con Anaconda Enviroment

Anaconda es un gestor de paquetes y un administrador de entorno de desarrollo para Python, es principalmente usado en proyectos de ciencia de datos debido a su gran cantidad de herramientas, en este caso servirá como ambiente de desarrollo para las librerías de web scraping.

Los pasos de instalación de anaconda son los siguientes, para este caso se utilizará la versión de anaconda en Windows la cual su instalación y configuración es mucho mas sencilla que en distribuciones GNU/LINUX.

1. Diríjase al sitio web de anaconda y elija el sistema operativo en el que se va a instalar anaconda, deberá ver una imagen como la siguiente.
**Figura 10.** Sitio web de descarga de Anaconda

![Figura_10](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_10.PNG)

2. Ahora ejecute el archivo instalable descargado anteriormente, allí deberá ver un asistente para la instalación que se vera de la siguiente manera.

**Figura 11.** Instalación de Anaconda en Windows parte 1

![Figura_11](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_11.PNG)

3. Haga click en Next y a continuación tendrá que leer el contrato de licencia, debe aceptar el contrato para proceder con la instalación.

**Figura 12.** Instalación de Anaconda en Windows parte 2

![Figura_12](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_12.PNG)

4. Después deberá especificar la ruta donde va a almacenar los binarios de Anaconda

**Figura 13.** Instalación de Anaconda en Windows parte 3

![Figura_13](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_13.PNG)

5. Deje marcadas las casillas como vienen por defecto debido a que marcar anaconda como variable de entorno implicaría siempre ejecutarlo por medio de comandos Shell

**Figura 14.** Instalación de Anaconda en Windows parte 4

![Figura_14](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_14.PNG)

6. Si todos los pasos de instalación fueron exitosos deberá ver la siguiente imagen

**Figura 15.** Instalación de Anaconda en Windows parte 5

![Figura_15](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_15.PNG)

Verifique que la instalación fue correcta abriendo su Power Shell e introduciendo los siguientes comandos, de ser exitosa la instalación y de tener bien configuradas las variables de entorno debería ver la siguiente imagen.

**Figura 16.** Comprobación del funcionamiento de Anaconda

![Figura_16](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_16.PNG)

Si los pasos anteriores fueron correctos ya puede ver un icono de una aplicación llamada Anaconda Navigator, al abrirla se encontrará con un administrador de aplicaciones del ambiente Anaconda y Python.

### 4.3 Instalación Jupyter Lab

Ahora que esta casi listo el ambiente de desarrollo local, necesitará un editor de código que le permita compilar código Python y aparte de eso este deberá ser compatible con todas las librerías que ocupa el proyecto.

Jupyter lab o anteriormente conocido como Jupyter notebook es un cuaderno digital donde se pueden compilar pequeñas piezas de código de manera simultanea o dividida sin afectar el resto del código, la instalación de Lupyter lab es realmente sencilla, necesitara abrir Anaconda Navigator y después simplemente instarlo.

**Figura 17.** Panel de aplicaciones Anaconda Navigator

![Figura_17](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_17.PNG)

Teniendo Jupyter listo para iniciar a desarrollar, su interfaz es bastante intuitiva, este se va a ejecutar en su navegador predeterminado, debería verse de la siguiente manera.

**Figura 18.** Interfaz gráfica Jupyter Lab

![Figura_18](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_18.PNG)

En la imagen anterior puede observar que a la izquierda esta el directorio de archivos en este caso del proyecto, en este panel de archivos y carpetas podrá crear y modificar archivos Jupyter bajo la extensión ipynb.

Ahora para compilar y ejecutar código deberá seleccionar un archivo con extensión ipynb y compilarlo de la siguiente manera.

**Figura 19.** Interfaz del editor de código Jupyter Lab

![Figura_19](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_19.PNG)

Podrá ejecutar bloques de código como se ve en la imagen anterior haciendo click sobre el icono de ejecutar o con las teclas alt + enter los resultados de la compilación los deberá ver debajo del bloque de código compilado como se ve en la imagen.

### 4.4 Repositorio del código del proyecto

Para acceder al código del proyecto con fines experimentación el proyecto cuenta con una licencia GPL V3 la cual se traduce a una licencia de código abierto es decir que se tendrán algunas libertades sobre el código del proyecto siempre y cuando se respeten los derechos de propiedad intelectual.

El repositorio del código del motor de búsqueda está alojado en Git Hub y esta disponible en el siguiente enlace: https://github.com/criss201x/Motor_busqueda_ETL/tree/dev allí encontrara el código de todas técnicas de extracción de datos implementadas, puede clonar el repositorio con el siguiente comando:

**Figura 20.** Clonado del repositorio

![Figura_20](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_20.PNG)

De esta manera podrá trabajar los archivos originales del proyecto en un entorno local y compilarlos en Jupyter Notebook como se vio en los pasos anteriores.

Si no desea clonar el repositorio y lo que busca únicamente es revisar el código de manera legible, desde el repositorio Git Hub del proyecto puede navegar desde una vista de usuario amigable de la siguiente manera.

**Figura 21.** Interfaz del código en Git Hub

![Figura_21](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_20.PNG)

De esta manera podrá observar tanto el código como el resultado de la compilación en la web sin necesidad de tener que realizar el proceso.

Moverse por la aplicación web de Git Hub es muy sencillo, puede acceder al contenido de la imagen anterior desde el siguiente enlace: https://github.com/criss201x/Motor_busqueda_ETL/blob/dev/Limpieza_y_carga_de_datos/
limpieza_de_datos_consolidado.ipynb

### 4.5 Desarrollo del lado del cliente

Si como desarrollador lo que desea es cambiar elementos o agregar nuevos elementos a la interfaz de usuario puede hacerlo teniendo conocimientos en Javascript, html y css, el framework que usa el proyecto es una mezcla de los tres anteriores bajo una arquitectura simple, inicialmente deberá tener instalado visual studio code.

Asumiendo lo anterior tendrá que instalar el framework svelte pero antes deberá instalar node js y npm, eso se hace de la siguiente manera.

1. Diríjase al sitio web de node js y seleccione la opción de acuerdo al sistema operativo que este usando

**Figura 22.** Sitio web node.js

![Figura_22](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_21.PNG)

**Fuente:** tomado de https://nodejs.org/en/download/

2. Una vez termine de descargarse el instalador ubique este archivo y ejecútelo

3. Se le pedirá confirmación para una serie de pasos para todos pulse siguiente

4. Debe aceptar el contrato de términos de licencia marcando la casilla de aceptar

5. El instalador le pedirá una ubicación para la instalación confirme una ruta de su sistema operativo por lo general la carpeta que define por defecto estaría bien

6. Siga avanzando sobre los pasos de instalación con el botón siguiente hasta que se llegue al botón de finalizar, llegado ese punto es porque la instalación fue exitosa

7. Verifique la instalación de node js y npm desde el power Shell con los siguientes comandos

**Figura 23.** Verificación instalación Node js

![Figura_23](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_23.PNG)

Si los pasos anteriores fueron exitosos ahora tendrá un ambiente casi listo para programar en Javascript, aún falta instalar el framework Svelte, este se hará desde npm de la siguiente manera:

**Figura 24.** Instalación Svelte js

![Figura_24](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_24.PNG)

Finalmente, ya tiene el ambiente listo para desarrollar sobre la interfaz del proyecto, lo que debe hacer es clonar el repositorio de la siguiente manera:

**Figura 25.** Clonado del proyecto

![Figura_25](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_25.PNG)

Ahora deberá ubicarse en el directorio que acaba de clonar y ejecutar visual studio code, en principio debería ver un editor de código de la siguiente manera.

**Figura 26.** Visual studio code

![Figura_26](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_26.PNG)

Ahora podrá editar la interfaz programando en html css y javascript, tenga en cuenta que esos cambios se verán en local únicamente, para compilar un proyecto de svelte se hace con el siguiente comando.

**Figura 27.** Compilación del proyecto

![Figura_27](https://github.com/criss201x/Motor_busqueda_ETL/Assets/Figura_27.PNG)

De esta manera podrá editar y experimentar con el código del lado del cliente del motor de búsqueda de horarios y espacios académicos

### 5 RESULTADOS Y CONCLUSIONES

- Se logro demostrar lo intuitiva que es la interfaz de usuario por medio de explicar al detalle cada uno de sus componentes.
- Se logro evidenciar lo novedoso que es programar en el ambiente de Anaconda para Python 3, es extremadamente sencillo, aumentando así la productividad del desarrollador un 100%
- Gracias a que los desarrollos del lado del cliente y del lado de la base de datos están desacoplados, es más fácil para el desarrollador entenderlos.

### 6 BIBLIOGRAFÍA
