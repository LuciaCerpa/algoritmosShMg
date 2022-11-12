def ordenar(list):
    if len(list) > 1 :
        mitad = len(list) // 2
        
        izquierda = list[:mitad]
        derecha = list[mitad:]
        
        ordenar(izquierda)
        ordenar(derecha)
        mezclar(list, izquierda, derecha)
        
def mezclar(list, izquierda, derecha):
    indiceIzq = indiceDer = indiceList = 0
    
    while indiceIzq < len(izquierda) and indiceDer < len(derecha):
        if izquierda[indiceIzq] < derecha[indiceDer]:
            list[indiceList] = izquierda[indiceIzq]
            indiceIzq+=1
        else:
            list[indiceList] = derecha[indiceDer]
            indiceDer+=1
        indiceList+=1
    
    while indiceIzq < len(izquierda):
        list[indiceList] = izquierda[indiceIzq]
        indiceIzq+=1
        indiceList+=1
        
    while indiceDer < len(derecha):
        list[indiceList] = derecha[indiceDer]
        indiceDer+=1
        indiceList+=1                

datos = [8, 12, 1, 3, 5]

print(ordenar(datos))