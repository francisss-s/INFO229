#Uso avanzado de Git y GitHub

Reflejar un tutorial como el de github es complicado, por ende me apegue un poco a la teoria y a los comandos necesarios para trabajar con git y github

primero la definicion de uno:

Git: es un software de control de versiones diseñado por Linus Torvalds.
esto sirve para controlar y tener un registro de los distintos cambios que se hacen sobre un proyecto, programa, etc

github: En un nivel más alto, GitHub es un sitio web y un servicio en la nube que ayuda a los desarrolladores a almacenar y administrar su código, al igual que llevar un registro y control de cualquier cambio sobre este código

con esto, ya sabemos que es git y github, ahora crearemos un pequeño paso a paso desde la creacion de un repositorio hasta agregar,eliminar y controlar archivos en el repositorio

---

ahora para comenzar:
###guia git
1.- iniciar un repositorio vacio
    ```bash
    git init
    ```

2.- añadir un archivo especifico al repositorio
    ``` 
    git add “nombre_de_archivo”
    ```
    tambien para añardir todos los archivos al repositorio
    ``` 
    git add .
    ```

3.- Confirmar los cambios realizados al repositorio
    ```
    git commit –am “mensaje”
    ```
    "mensaje" sirve para agregar una descripcion breve al commit que se esta haciendo

4.- Obtener la lista de cambios echos
    ```
    git log -p
    ```
    con esto podemos saber el hash del commit

5.- remover un commit dado su hash
    ```
    it revert “hash_commit"
    ```
6.- Subir la rama(branch) “nombre_rama” al servidor remoto.
    ```
    git push origin “nombre rama”
    ```

7.- Mostrar el estado actual de la rama
    ```
    git status
    ```
8.- para actualizar tu repositorio local al commit mas nuevo
    ```
    git pull
    ```

con estos comandos podemos hacer un buen uso de git en nuestros proyectos


###Gia GitHub
para github es necesario tener una cuenta en el servicio, para asi poder mesclar estas herramientas

1.- para conectar a github
    es necesario logearse en su cuenta y crear un repositorio ahi, tener en cuenta el nombre y el link de donde se crearon.
    asi luego poder agregar un repositorio local a github con
    ```
    git remote add origin link
    ```
    ```
    git push -u origin master
    ```
con esto estarian conectados tanto el repositorio local como el de github

2.- obtener archivos del repositorio github
    en caso que no poseamos el repositorio de forma local necesitamos recuperar los archivos desde github
    ```
    git pull origin master
    ```

3.- hacer push a una rama hacia repositorio remoto 
    para enviar una rama al repositorio github
    ```
    git push origin my-new-branch
    ```

4.- para mesclar las ramas
    como al trabajar en un repositorio varias personas en ellas crearan distintas ramas, y puede ser el caso que necesites agregar tus archivos al repositorio
    ```
    git merge <nombre-rama>
    ``` 
