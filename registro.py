
import json

file_name = "users.json"


def mostrar_menu():
    print('')
    print('------------------------')
    print('MENU:')
    print('------------------------')
    print('1 - Crear usuario')
    print('2 - Iniciar sesion')
    print('3 - Salir')
    print('')

    init_file()

    opcion = input('Ingrese una opcion: ')

    if (opcion == '1'):
        crear_usuario()
    elif (opcion == '2'):
        iniciar_sesion()
    elif (opcion == '3'):
        exit()
    else:
        mostrar_menu()


def init_file():
    try:
        with open(file_name) as f:
            return json.load(f)
    except FileNotFoundError:
        f = open(file_name, "a")
        f.write(json.dumps([]))
        f.close()

        f = open(file_name, "r")
        return json.load(f)


def obtener_usuarios():
    # Como buscar usuario en el json
    f = open(file_name, "r")
    content = f.read()
    users = json.loads(content)
    f.close()

    return users


def crear_usuario():
    print('')
    print('------------------------')
    print('CREAR USUARIO: ')
    print('------------------------')
    nombre_usuario = input('Introducir un nombre de usuario: ')
    contrasena_usuario = input('Introducir contraseña: ')
    repetir_contrasenia = input('Repetir contreseña: ')

    if (contrasena_usuario != repetir_contrasenia):
        print('ERROR: Las contraseñas no coinciden!!')
        crear_usuario()

    # Agregar comprobacion si ya existe usuario con ese nombre aca
    users = obtener_usuarios()

    usuario_encontrado = None
    for user_in_list in users:

        # print('userInList: ', user_in_list)
        if user_in_list['username'] == nombre_usuario and user_in_list['password'] == contrasena_usuario:
            usuario_encontrado = user_in_list
            break

    if (usuario_encontrado != None):
        print('ERROR: Ya existe un usuario con ese nombre!! Intente con otro distinto.')
        crear_usuario()

    new_user = {'username': nombre_usuario, 'password': contrasena_usuario}

    users.append(new_user)

    f = open(file_name, "w")

    f.write(json.dumps(users))

    f.close()

    print('')
    print('USUARIO CREADO!!!')
    print('')

    mostrar_menu()


def iniciar_sesion():
    print('')
    print('------------------------')
    print('INICIAR SESION:')
    print('------------------------')
    nombre_usuario = input('Introducir un nombre de usuario: ')
    contrasena_usuario = input('Introducir contraseña: ')

    # Como buscar usuario en el json
    f = open(file_name, "r")

    users = json.loads(f.read())

    usuario_encontrado = None
    for user_in_list in users:

        # print('userInList: ', user_in_list)
        if user_in_list['username'] == nombre_usuario and user_in_list['password'] == contrasena_usuario:
            usuario_encontrado = user_in_list
            break

    if (usuario_encontrado == None):
        print('ERROR: Datos incorrectos.')
        iniciar_sesion()
    else:
        print('Usted ha iniciado sesion exitosamente!!')


mostrar_menu()
