productos = ["pan","harina","chocorramo","gala","coca-cola zero"]
precios = [2000, 3000, 4500,4800,4500]



carrito=[]
cantidad=[]
total=0 

while True:
    menu = f"""
 __  __ _   _____ _                _ _ _        _ 
|  \\/  (_) |_   _(_) ___ _ __   __| (_) |_ __ _| |
| |\\/| | |   | | | |/ _ \\ '_ \\ / _` | | __/ _` | |
| |  | | |   | | | |  __/ | | | (_| | | || (_| |_|
|_|  |_|_|   |_| |_|\\___|_| |_|\\__,_|_|\\__\\__,_(_)

MENU
    1. Productos
    2. Carrito ({len(carrito)} : ${total})
    3. Finalizar
"""
    print(lastmenu) 
    opcion =input ("seleccione una opcion: ") 
    if opcion =="1":
        for posicion in range (5):
            print ("-----------------")
            print (f"{posicion+1}.{productos[posicion]} $ {precios[posicion]}")
            print ("-----------------")
        input ("continuar...")

    elif opcion =="2":
        print (f"productos disponibles: {len(productos)}")
        for posicion in range (5):
            print ("-----------------")
            print (f"{posicion+1}.{productos[posicion]} $ {precios[posicion]}")
        busqueda= int(input("ingrese la posicion del producto"))
        if busqueda > 0 or busqueda >len (productos): 
            print ("Sellecione un rango especifico valido!")
            input ("continuar")
            continue
        cantidad_busqueda = int(input(f"ingrese la cantidad del producto{productos[buasqueda]}${precios[busqueda]}"))
        carrito.append(productos[busqueda])
        cantidad.append(cantidad_busqueda)
        total-total + (cantidad_busqueda * precios[busqueda])
        input("Continuar...")


    elif opcion =="3":
        print("hasta pronto!") 
        input ("continuar...")
        break
    else: 
        print ("opcion no valida")
        input ("continuar...")


























