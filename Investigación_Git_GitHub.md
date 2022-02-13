![TAREA](https://tortoizthemes.com/wp-content/uploads/2020/09/cover-pic.jpeg)


# INVESTIGACIÓN GIT/GITHUB WN9630850

## Git
Git es un sistema de control de versiones, lo que eso significa realmente es que Git nos ayuda a gestionar nuestros archivos de proyecto. Una de las cosas principales que hace Git y también la razón principal por la que existe es para mantener un registro de toda la historia de las cosas en las que estás trabajando.

Esto es especialmente útil para los desarrolladores porque cuando estás trabajando en un proyecto primero construyes una versión básica del mismo y luego tratas de mejorarlo añadiendo nuevas características o simplemente experimentando con las cosas. Todo este proceso de experimentar con nuevas características es increíblemente propenso a errores y es posible que desee volver a su código original.

Aquí es donde el control de versiones entra en juego, realiza un seguimiento automático de cada minuto de cambio en tu proyecto y nos permite volver a una versión anterior sin importar cuántas veces haya cambiado sus archivos.

Otra cosa asombrosa que Git permite hacer es que permite a las personas trabajar juntos en el mismo proyecto al mismo tiempo sin perturbar los archivos de los demás. La colaboración es aún más fácil con Git, los miembros de un equipo pueden trabajar en diferentes características y fusionar fácilmente los cambios.

## GitHub
GitHub es un servicio basado en la web para el control de versiones usando Git. Básicamente, es un sitio de redes sociales para desarrolladores. Puedes mirar el código de otras personas, identificar los problemas con su código e incluso proponer cambios. Esto también le ayuda a mejorar su código. En una nota más ligera, es un gran lugar para mostrar tus proyectos y ser notado por los reclutadores potenciales.


## ¿Cuál es la diferencia entre Git y GitHub?
Git es una herramienta de control de versiones distribuida que puede gestionar el historial de código fuente de un proyecto de desarrollo, mientras que GitHub es una plataforma basada en la nube construida alrededor de la herramienta Git.

(https://flic.kr/p/2fur2Pu) 


## ¿Qué es el control de versiones?
Un sistema de control de versiones es una herramienta que gestiona los cambios realizados en los archivos y directorios de un proyecto. Existen muchos sistemas de control de versiones; esta lección se enfoca en uno llamado Git, que es utilizado por muchas de las herramientas de ciencia de datos que se tratan en nuestras otras lecciones. 

#### Sus puntos fuertes son:
- Nunca se pierde nada de lo que se guarda en Git, por lo que siempre puede regresar para ver qué resultados fueron generados por qué versiones de sus programas.
- Git te notifica automáticamente cuando tu trabajo entra en conflicto con el de otra persona, por lo que es más difícil (pero no imposible) sobrescribir el trabajo accidentalmente.
-	Git puede sincronizar el trabajo realizado por diferentes personas en diferentes máquinas, por lo que escala como lo hace su equipo.

El control de versiones no es solo para el software: libros, documentos, conjuntos de parámetros y cualquier cosa que cambie con el tiempo o necesite compartirse puede y debe almacenarse y compartirse usando algo como Git.

## Flujo de trabajo en GIT

![Flujo](https://miro.medium.com/max/1000/0*HeEKExh4Z0nlev1m.png)

## ¿Dónde almacena Git la información?
Cada uno de sus proyectos de Git tiene dos partes: los archivos y directorios que crea y edita directamente, y la información adicional que registra Git sobre el historial del proyecto. La combinación de estas dos cosas se llama repositorio.
Git almacena toda su información adicional en un directorio llamado .git ubicado en el directorio raíz del repositorio. Git espera que esta información se presente de manera muy precisa, por lo que nunca debes editar ni eliminar nada en .git.


## ¿Cómo puedo comprobar el estado de un repositorio?
Cuando esté utilizando Git, con frecuencia querrá verificar el estado de su repositorio. Para ello, ejecute el comando git status, que muestra una lista de los archivos que se han modificado desde la última vez que se guardaron los cambios.
Usted ha sido puesto en el repositorio dental. Use el estado de git para descubrir qué archivos se han cambiado desde la última vez que se guardó. ¿Qué archivo(s) se enumeran?

## ¿Cómo puedo saber lo que he cambiado?
Git tiene un área de preparación en la que almacena archivos con cambios que desea guardar y que aún no se han guardado. Poner archivos en el área de preparación es como poner cosas en una caja, mientras que confirmar esos cambios es como poner esa caja en el correo: puede agregar más cosas a la caja o sacar cosas con la frecuencia que desee, pero una vez que las coloca en el correo, no puede hacer más cambios.

git status le muestra qué archivos están en esta área de preparación y qué archivos tienen cambios que aún no se han colocado allí. Para comparar el archivo tal como está actualmente con lo que guardó por última vez, puede usar git diff filename. git diff sin ningún nombre de archivo le mostrará todos los cambios en su repositorio, mientras que el directorio git diff le mostrará los cambios en los archivos en algún directorio.

# COMANDOS MAS UTILIZADOS EN GIT

## Git clone
Git clone es un comando para descargarte el código fuente existente desde un repositorio remoto (como Github, por ejemplo). En otras palabras, Git clone básicamente realiza una copia idéntica de la última versión de un proyecto en un repositorio y la guarda en tu ordenador.

Hay un par de formas de descargar el código fuente, pero principalmente yo prefiero clonar de la forma con https: git clone 
```
<https://link-con-nombre-del-repositorio>
```
Por ejemplo, si queremos descargar un proyecto desde Github, todo lo que necesitamos es hacer clic sobre el botón verde (clonar o descargar), copiar la URL de la caja y pegarla después del comando git clone que he mostrado más arriba.

bootstrap-github-1
Código fuente de Bootstrap en Github
Esto hará una copia del proyecto en tu espacio de trabajo local y así podrás empezar a trabajar con él.

## Git branch
Las ramas (branch) son altamente importantes en el mundo de Git. Usando ramas, varios desarrolladores pueden trabajar en paralelo en el mismo proyecto simultáneamente. Podemos usar el comando git branch para crearlas, listarlas y eliminarlas.

Creando una nueva rama:
```
git branch <nombre-de-la-rama> 
```
Este comando creará una rama en local. Para enviar (push) la nueva rama al repositorio remoto, necesitarás usar el siguiente comando:
```
git push <nombre-remoto> <nombre-rama>
```
Visualización de ramas:
```
git branch
```
```
git branch --list
```
Borrar una rama:
```
git branch -d <nombre-de-la-rama>
```

## Git checkout
Este es también uno de los comandos más utilizados en Git. Para trabajar en una rama, primero tienes que cambiarte a ella. Usaremos git checkout principalmente para cambiarte de una rama a otra. También lo podemos usar para chequear archivos y commits.
```
git checkout <nombre-de-la-rama>
```
Hay algunos pasos que debes seguir para cambiarte exitosamente entre ramas:

Los cambios en tu rama actual tienen que ser confirmados o almacenados en el guardado rápido (stash) antes de que cambies de rama.
La rama a la que te quieras cambiar debe existir en local.
Hay también un comando de acceso directo que te permite crear y cambiarte a esa rama al mismo tiempo:
```
git checkout -b <nombre-de-tu-rama>
```
Este comando crea una nueva rama en local (-b viene de rama (branch)) y te cambia a la rama que acabas de crear.

## Git status
El comando de git status nos da toda la información necesaria sobre la rama actual.
```
git status
```
Podemos encontrar información como:

* Si la rama actual está actualizada
* Si hay algo para confirmar, enviar o recibir (pull).
* Si hay archivos en preparación (staged), sin preparación(unstaged) o que no están recibiendo seguimiento (untracked)
* Si hay archivos creados, modificados o eliminados

git-status-1
git status nos da información acerca del archivo y las ramas

## Git add
Cuando creamos, modificamos o eliminamos un archivo, estos cambios suceden en local y no se incluirán en el siguiente commit (a menos que cambiemos la configuración).

Necesitamos usar el comando git add para incluir los cambios del o de los archivos en tu siguiente commit.

Añadir un único archivo:
```
git add <archivo>
```
Añadir todo de una vez:
```
git add -A
```
Si revisas la captura de pantalla que he dejado en la sección 4, verás que hay nombres de archivos en rojo - esto significa que los archivos sin preparación. Estos archivos no serán incluidos en tus commits hasta que no los añadas.

Para añadirlos, necesitas usar el git add:

git-add
Los archivos en verde han sido añadidos a la preparación gracias al git add
Importante: El comando git add no cambia el repositorio y los cambios que no han sido guardados hasta que no utilicemos el comando de confirmación git commit.

## Git commit
Este sea quizás el comando más utilizado de Git. Una vez que se llega a cierto punto en el desarrollo, queremos guardar nuestros cambios (quizás después de una tarea o asunto específico).  

Git commit es como establecer un punto de control en el proceso de desarrollo al cual puedes volver más tarde si es necesario.

También necesitamos escribir un mensaje corto para explicar qué hemos desarrollado o modificado en el código fuente.
```
git commit -m "mensaje de confirmación"
```
Importante: Git commit guarda tus cambios únicamente en local.

## Git push
Después de haber confirmado tus cambios, el siguiente paso que quieres dar es enviar tus cambios al servidor remoto. Git push envía tus commits al repositorio remoto.
```
git push <nombre-remoto> <nombre-de-tu-rama>
```
De todas formas, si tu rama ha sido creada recientemente, puede que tengas que cargar y subir tu rama con el siguiente comando:
```
git push --set-upstream <nombre-remoto> <nombre-de-tu-rama>
```
o
```
git push -u origin <nombre-de-tu-rama>
```
Importante: Git push solamente carga los cambios que han sido confirmados.

## Git pull
El comando git pull se utiliza para recibir actualizaciones del repositorio remoto. Este comando es una combinación del git fetch y del git merge lo cual significa que cundo usemos el git pull recogeremos actualizaciones del repositorio remoto (git fetch) e inmediatamente aplicamos estos últimos cambios en local (git merge).
````
git pull <nombre-remoto>
````
Esta operación puede generar conflictos que tengamos que resolver manualmente.

## Git revert
A veces, necesitaremos deshacer los cambios que hemos hecho. Hay varias maneras para deshacer nuestros cambios en local y/o en remoto (dependiendo de lo que necesitemos), pero necesitaremos utilizar cuidadosamente estos comandos para evitar borrados no deseados.

Una manera segura para deshacer nuestras commits es utilizar git revert. Para ver nuestro historial de commits, primero necesitamos utilizar el  git log -- oneline:

histo-rico-git
histórico de git en mi rama master
Entonces, solo necesitamos especificar el código de comprobación que encontrarás junto al commit que queremos deshacer:
````
git revert 3321844
````
Después de esto, verás una pantalla como la de abajo -tan solo presiona shift + q para salir:

resim-2
El comando git revert deshará el commit que le hemos indicado, pero creará un nuevo commit deshaciendo la anterior:

git-revert
commit generado con el git revert
La ventaja de utilizar git revert es que no afecta al commit histórico. Esto significa que puedes seguir viendo todos los commits en tu histórico, incluso los revertidos.

Otra medida de seguridad es que todo sucede en local a no ser que los enviemos al repositorio remoto. Por esto es que git revert es más seguro de usar y es la manera preferida para deshacer los commits.

## Git merge
Cuando ya hayas completado el desarrollo de tu proyecto en tu rama y todo funcione correctamente, el último paso es fusionar la rama con su rama padre (dev o master). Esto se hace con el comando git merge.

Git merge básicamente integra las características de tu rama con todos los commits realizados a las ramas dev (o master).  Es importante que recuerdes que tienes que estar en esa rama específica que quieres fusionar  con tu rama de características.

Por ejemplo, cuando quieres fusionar tu rama de características en la rama dev:

Primero, debes cambiarte a la rama dev:
````
git checkout dev
````
Antes de fusionar, debes actualizar tu rama dev local:
````
git fetch
````
Por último, puedes fusionar tu rama de características en la rama dev:
````
git merge <nombre-de-la-rama>
````
## EJEMPLO DEL FLUJO DE COMANDOS EN GIT

![](https://miro.medium.com/proxy/1*D1lbqiz2Y6quKrt00p9DqQ.png)
________

*Bibliografia*

1. https://www.xataka.com/basics/que-github-que-que-le-ofrece-a-desarrolladores
2. https://www.youtube.com/watch?v=oxaH9CFpeEE
3. https://code.visualstudio.com/docs/?dv=win


Notas:
>Previo a la investigación, tambien se estudió el uso de Markdown, seleccionando VISUAL STUDIO CODE, el cual me pareció muy facil de utilizar y con una interfaz y visualización que permite comprender rapidamente su funcionalidad para luego crear el archivo .MD con la investigación del curso.


[Link_Repositorio_WN9630850](https://github.com/Walnabra/Galileo)
