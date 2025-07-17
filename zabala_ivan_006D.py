productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}
def stock_marca (marca):
    claves = []
    total = 0
    for c, v in productos.items():
        if v [0].lower():
            total += stock [c] [1]
            claves.append(c)
            print(f"stock de marca{marca()}es de {total} " )
def busqueda_precio(p_min,p_max):
    try:
        p_min=int(p_min)
        p_max=int(p_max)
        ordenados=[]
        for c,v in stock.item():
            if (v [0] >= p_min and v [0] <= p_max)and v [1] >0:
                ordenados.append(productos[c][0]+ " "+c)
        ordenados.sort()
        if len(ordenados)>0:
            print("no hay producto en ese rango de precios")
        else: 
            for i in ordenados:
                print (i)
    except: 
            print ("debe ingresar valores enteros")
def actualizar_precio(modelo,p):
    if modelo in stock:
        stock [modelo][0]=p
        return True
    else:
        return False
while True:
    modelo = input("ingrese el modelo del producto: ")
    precio = int(input("ingrese nuevo precio: "))
    if actualizar_precio(modelo,precio):
        print("precio actualizado ")
    else:
        print("el producto no existe ")
    if input("desea actualizar otro precio(si/no)")=="no":
       print("gracias")
    if input("escriba salir para salir")=="salir":
       print("Programa finalizado")   
    break



        


            

