def unlogin_command(sesion_activa, usuario_registrado):
    print("----------------------------------------------------------")
    print("Comando unlogin en ejecucion")

    if(sesion_activa):
        print("Sesión cerrada con exito")
        usuario_registrado.pop(0)
        return False
    else:
        print("No existe una sesesion iniciado, por lo que no es posible aplicar el comando logout")
        return sesion_activa
    