ListaDeNombres = ["Frank", "José", "Pepe", "Juancarlo Estebanizes", "Johnnsito perez", 
                  "Juancarlo ronaldo",]
nombres_seleccionados = ListaDeNombres[2:]
print(nombres_seleccionados)
# LAS LISTAS SIEMPRE EMPIEZAN POR EL 0
#al parecer si pongo 2 empieza a listar del nombre 3 (?)
#esta marcado 2 y el nombre 2 es José (el 3 es pepe)
#que despues de los dos puntos (:) no haya nada significa que se listara del 2 en adelante
#cualquier valor vacio antes o despues de los dos puntos (:) es del inicio (izquierda) o del final
#(derecha)
#tambien se puede poner algo como [1:6:2] esto dignifica que:
# 0 1 2 3 4 5 6 (←index)
# x v x v x v
# x =  salto
ListaDeNombres = ["Frank", "José", "Pepe", "Juancarlo Estebanizes", "Johnnsito perez", 
                  "Juancarlo ronaldo",]
nombres_seleccionados = ListaDeNombres[::-1]
print(nombres_seleccionados)