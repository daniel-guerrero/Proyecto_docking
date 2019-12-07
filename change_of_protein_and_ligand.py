import os
import sys
import shutil

#print("inicio")
def leer_carpe(carpeta):
    return os.listdir(carpeta)


def listar(lista):
    lista_solo = []
    for j in lista:
        lista_solo.append(j.split(".")[0])
    return lista_solo

print("segunda etapa")

def copiar_carpe(lista_solo, carpeta_destino):
    os.mkdir(carpeta_destino)
    for k in lista_solo:
        os.mkdir(sys.argv[2] + '/' + k)


#print("tercera etapa")


def listar_ligando(complejos, lista_carpetas):
    ligando_solo = []
    os.chdir(complejos)
    for carpeta in lista_carpetas:
        os.chdir(carpeta)
        ligando = os.listdir("LIG")
        ligando_solo.append(ligando)
        os.chdir('..')
    os.chdir("..")
    return ligando_solo
     



def copiar_prot_lig(lista_sin_extencion, proteina, ligando, complejos, carpeta_destino):
    i=0
    for carpetas in lista_sin_extencion:
        base = complejos + '/' + lista_sin_extencion[i] + '/PROT/'
        origen_prot = base  + proteina[i]
        destino_prot = carpeta_destino + '/' + lista_sin_extencion[i]
        if path.exists(origen_prot):
            shutil.copy(origen_prot, destino_prot)
            print("already!!")
            i+=1
        else:
            print("no existe")
            i+=1
            pass
        base_1 = complejos + '/' + lista_sin_extencion[i] + '/LIG/'
        origen_lig = base_1 + ligando[i]
        destino_lig = carpeta_destino + '/' + lista_sin_extencion[i]
        if path.exists(origen_lig):
            shutil.copy(origen_lig, destino_lig)
            print("already!!")
            i+=1
        else:
            print("no existe")
            i+=1
            pass
     

     
### inicialización de variables
### Llamadas de funciones
carpeta_archivos = sys.argv[1]
carpeta_destino = sys.argv[2]
proteina = leer_carpe(carpeta_archivos)
lista_sin_extencion = listar(proteina)
complejos = sys.argv[3]
ligando = listar_ligando(complejos, lista_sin_extencion)


copiar_carpe(lista_sin_extencion, carpeta_destino)
copiar_prot_lig(lista_sin_extencion, proteina, complejos, carpeta_destino, ligando)






