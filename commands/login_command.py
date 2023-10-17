def login_command(user_login, pass_login, id_option, list_mount, sesion_activa, list_users, usuario_registrado):
    print("----------------------------------------------------------")
    print("Comando login en ejecucion con los siguientes parametros:")
    print(f"User: {user_login}")
    print(f"Pass: {pass_login}")
    print(f"Id: {id_option}")
    if(sesion_activa):
        "Actualmente se encuentra una sesion iniciada."
    find = False
    path_dsk = None
    partition_size = None
    partition_start = None
    for partition in list_mount:
        if id_option == partition["id"]:
            path_dsk = partition["path"]
            partition_size = partition["size"]
            partition_start = partition["start"]
            find = True
            
    if find:
        pass
    else:
        print(f"Particion {id_option} no encontrado en las particiones montadas, por lo que no es posible ejecutar mkfs.")
        return False
    for partition in list_users:
        if str(partition["user"])==user_login and str(partition["password"])==pass_login:
            sesion_activa = True
    
    if sesion_activa:
        print("Inicio de sesion exitoso")
        usuario_registrado.append({"user": user_login, "password": pass_login, "id": id_option})
        return sesion_activa
    else:
        print("Las credenciales ingresadas son incorrectas")
        return sesion_activa