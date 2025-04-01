list=["apple","watermelon","peach","kiwi","strawberry"]
list_2=[
    ["january","february","march"],
    ["april","june","july"],
    ["august","september","may"],
    
]
#acceder
print(list[1])
print(list_2[1][1])
#insertar
list.insert(3,"Estructura de datos" )
print(list)
#borrar
del list_2[2][2]
print(list_2)
#busqueda
print(list.index("Estructura de datos"))
print(list_2[0].index("january"))
