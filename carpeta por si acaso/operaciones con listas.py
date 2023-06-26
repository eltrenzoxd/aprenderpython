ListaNumerica=[69,420,69420,42069,64209,123456789,0.987654321,3.14159265359]
ListaNumerica.sort()
print (ListaNumerica)

ListaNumerica=[69,420,69420,42069,64209,123456789,0.987654321,3.14159265359]
ListaNumerica.sort(reverse=True)
print (ListaNumerica)
#tambien se puede usar asi↓
ListaNumerica=[69,420,69420,42069,64209,123456789,0.987654321,3.14159265359]
ListaNumerica.sort()
menor = ListaNumerica[0]
print (menor)
#y vice versa
#otras maneras de sacar mayor o menor en una lista
mayor = max(ListaNumerica)
print (mayor)

menor = min(ListaNumerica)
print (menor)
#se puede sacar la longitud de la lista
longitud =len(ListaNumerica)
print(longitud)
#y tambien se pueden encontrar numeros y su indice (true=si existe y false=no existe)
result = 69420 in(ListaNumerica)
print(result)

int = ListaNumerica.index(69420)
print(int)