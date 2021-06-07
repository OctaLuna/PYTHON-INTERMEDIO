def main():
    #Estamos creando una lista
    my_List = [3.1415926535, "HOLA MUNDO", False, 73]
    #Estamos creando un diccionario
    my_dict = {"Firstname": "Octavio", "Lastname": "Luna"}

    #Ahora vamos a hacer una locura, vamos a poner diccionarios dentro de listas y listas dentro de diccionarios
    #Vamos a crear 2 estructuras mas
    super_List = [
        {"Firstname": "Octavio", "Lastname": "Luna"},
        {"Firstname": "Huascar", "Lastname": "Luna"},
        {"Firstname": "Alejandra", "Lastname": "Luna"},
        {"Firstname": "Andrea", "Lastname": "Luna"},
    ]
    super_Dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, 1, 2, 0, -8],
        "floating_nums": [1.1, 5.8, 7.6, 9.4]
    }

    #Esto e para mostrar el super dict
    #Items es para recorer las llaves y valores al mismo tiempo de un diccionario
    #key, value Esto es para mostrar los valores de el diccionario, Key es su llave "Es el nombre que tiene" y value es su valor
    for key, values in super_Dict.items():
        print(key, "-", values)
    for values in super_List:
        for key, values in values.items():
            print(key, ":", values)
    #Pass es cuando no vamos a escribir codigo en la funcion
    #pass




#Esto es para iniciar la funcion cuando nosotros ejecutamos nuestro archivo de python
if __name__ == '__main__':
    main()