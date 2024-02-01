El archivo seqClass.py nos permite identificar si una cadena es DNA o RNA. Además, también nos localiza los motif que hay dentro de dicha cadena (introducida por el usuario).
También hay comentarios de código para poder entender paso a paso lo que hace el código.

Se ha practicado con el seqClass.py. Hemos aprendido:
- git status: ver lo que tengo (verde: todo OK, no se ha hecho ninguna modificación; rojo: se ha hecho alguna modificación; nada: no hemos hecho nada)
- git add: añadir/actualizar la modificación
- git commit -m "comentario": guardar la modificación + un comentario
- git log <namefile>: ver el historial (las modificaciones que se han hecho)
- git checkout: para volver atrás (hasta el último commit). Si no se ha hecho commit.
- git checkout <namebranch>: para cambiar de brangh
- git branch: para ver en qué branch estamos
- git branch <namebranch>: para crear un branch nuevo
- git reset: para volver hacia atrás (por si nos hemos equivocado)
- git revert: para eliminar el último commit. Se queda registrado
- git merge <branchname>: primero hay que estar en el branch que quiero actualizar (git checkout namebranch). <branchname> es el que tiene los cambios que quiero incorporar
- git push -u origin master: para subir un repositorio local a remoto (GitHub)
- git pull: para actualizar un repositorio local (de remoto a local. Por lo tanto, hemos hecho la modificación en el remoto, y ahora lo queremos también en el local)
- git clone: para obtener una copia local de un repositorio remoto de otra persona
