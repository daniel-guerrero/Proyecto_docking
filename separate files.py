import sys
def leer(archivo):
    abrir = open(archivo, "r")
    leer_prot = open("prot.pdb", "w")
    leer_lig = open("lig.pdb", "w")
    for i in abrir:
        leer_linea = i.split()
        if leer_linea[0] == "ATOM":
            print("proteina --> listo")
            leer_prot.write(i)
        elif leer_linea[0] == "HETATM":
            print("ligando --> listo")
            leer_lig.write(i)
    leer_prot.close()
    leer_lig.close()




leer("2qzl.pdb")














    

