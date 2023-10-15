from Password import Password

listPassword = list()

for numero in range(1,3):
    longitud = input("ingrese longitud de la password : ")

    parsedInt = int(longitud)

    if( parsedInt > 6 and parsedInt < 16):
        passwordNueva = Password(parsedInt)
    else:
        passwordNueva = Password()

    listPassword.append(passwordNueva)

for password in listPassword:
    print(password)