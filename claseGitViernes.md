# GIT
* https://docs.google.com/presentation/d/1uIaORmJHMwUHozEQMDqJbGDKc48FZVsD7Rn8GIm8cl4/edit#slide=id.g299e8b56e3_0_345
* Es un sistema de control de versiones
 * Permite mantener diferentes versiones históricas de nuestros archivos
 * Podemos "Regresar en el tiempo"
 * Sandboxing: permite tener un entorno seguro
 * Blaming: Mantiene registro de quién y cuándo hizo cambios
 * Branching: Diferentes versiones actuales del mismo proyecto
 * Sharing: Compartimos el código
* Algunas plataformas parecidas:
 * Gitlab, gitbucket
* No necesariamente es solo para código

---

### Ejercicio Git
* En la carpeta "mi-proyecto"
 * git init
* Para asociar nuestra cuenta de github con git:
 * git config --global user.name "ledzerck"
 * git config --global user.email "aldomapler@gmail.com"

#### Workflow
* Working directory
 * Contiene los archivos de nuestro proyecto
* Staging area
 * Área de preparación
* Respository
 * Cambios confirmados y guardados


* git status
 * Nos dice en que estado se encuentra nuestro repositorio
* git add .
 * Agrega los archivos a la área de preparación
* git commit -m "Mensaje describiendo los cambios"
 * Guarda los archivos en el repositorio y nos deja describir los cambios

#### Local y Remote
* El local es el que se encuentra en nuestra computadora
* El remoto es el que ya está en el servidor y se le suele llamar origin


* ir a Github y crear un nuevo repositorio
 * Pegar la línea de comando en terminal:
   * git remote add origin git@github.com:ledzerck/mi-proyecto.git
   * Con esto ligamos nuestro repo local con el remoto
* git push origin master
* El origin tiene que estar con https


#### Otros comandos
* git clone
 * Permite clonar repositorios
* git pull
 * Trae los cambios desde el servidor
* git checkout
 * nos deja movernos entre ramas de un proyecto
* git merge
 * fusiona los cambios realizados en dos ramas
* git ignore
 * Indicamos que archivos queremos dejar sin seguimiento
 


---

*Buscar plática de TED sobre linux (Linus Torvald)*
