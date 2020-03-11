#Uso de la funcion format
intBase = 7
intAltura = 5
fltAreaTriangulo=(intBase*intAltura)/2
txt = "Area: {2:0.2f} ( {0} por {1} entre dos)"
#Valores incrustados en la salida
print (txt.format(intBase, intAltura, fltAreaTriangulo))