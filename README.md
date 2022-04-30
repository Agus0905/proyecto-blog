# proyecto-blog
Proyecto final pt1

Proyecto creado en: Django, Python, Html. JavaScript

Proyecto con finalidad de Blog. Posee funcionalidades de registracion y login de usuario. Modificar el perfil, que cada usuario tenga accessos a diferentes funcionalidades. Poder editar y borrar un post que el mismo usuario haya creado. La division en categoriass de los posts, etc.

#Blog

blog/<int:pk> - Pagina donde se ve en detalle cada post. PK, primary key para poder idientificar y seleccionsar automaticamente en que post nos meteremos.
 add_post/- Pagina donde se podra crear un post(siempre y cuando el usuario este logeado)
post/edit/<int:pk> - Pagina para editar el blog creado(simpre y cuando el usuario este logeado y sea un post propio)
post/<int:pk>/delete - Pagina para editar el blog creado(simpre y cuando el usuario este logeado y sea un post propio)
add_category/ - Pagina para agregar categorias
category/<str:cats>/ - Pagina para ver los posts en cada categoria
category_list/' - Pagina con lista de categorias
like/<int:pk> - funcionalidad creada dentro del detalle de pagina donde el usuario(logeado) pueda darle like o quitar su like de una publicaicon
blog/<int:pk>/comment/ - funcionalidad creada dentro del detalle de pagina donde el usuario pueda comentar una publicacion
search_bar/ - Barra de busqueda para filtrar de todos los posts el que queramos ver
'about/ - Pagina donde se habla del autor de la pagina
