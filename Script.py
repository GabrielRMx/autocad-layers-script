#######################################
########### ALBANY ORTUÑEZ ############
#######################################


import ezdxf

def comprobar_valor(layer, grosor):
    grosor_a_comprobar = int(grosor)
    
    try:
        layer.dxf.lineweight = int(grosor)
    except ValueError:
        print("Por favor ingrese un valor numérico para el grosor.")
    except Exception as e:
        print(f"Error al asignar grosor: {e}")
    finally:
        print(f"Grosor de {layer.dxf.name}: {grosor} mm asignado...")
                

def asignar_grosor_capas(archivo_dwg):
    
    # Cargar el archivo DWG
    doc = ezdxf.readfile(archivo_dwg)

    # Obtener todas las capas
    layers = doc.layers

    # Mostrar todas las capas y permitir asignar un grosor
    print("ASIGNANDO VALORES POR DEFECTO...\n")
    for layer in layers:
            
            if layer.dxf.name == "- PAREDES":
                nombre_de_capa = layer
                grosor = 50
                comprobar_valor(nombre_de_capa, grosor)
                    
            if layer.dxf.name == "- PUERTAS":
                nombre_de_capa = layer
                grosor = 30
                comprobar_valor(nombre_de_capa, grosor)
                    
            if layer.dxf.name == "Ventanas":
                nombre_de_capa = layer
                grosor = 30
                comprobar_valor(nombre_de_capa, grosor)
                
    # Permitir al usuario elegir el valor a asignar para cada capa.                
    terminar_programa = False
    
    while terminar_programa != True:
        
        opc = input("\nAsignar valores manualmente? Si / No: ")
        
        if opc.lower() == "si":
            
            capa = input("Nombre de la capa: ")
            nuevo_grosor_de_capa = 0
            
            for layer in layers:
                
                if capa == layer.dxf.name:
                    print(f"Asignando nuevo valor a la capa → {capa}\n")
                    nuevo_grosor_de_capa = int(input("Nuevo grosor: "))
                    comprobar_valor(layer, nuevo_grosor_de_capa)
                    break
            
        else:
            print("Cerrando script...")
            terminar_programa = True
                
    # Guardar los cambios
    doc.saveas(archivo_dwg)

if __name__ == "__main__":
    archivo_dwg = "colegio.dxf"  # Reemplaza con tu archivo DWG
    asignar_grosor_capas(archivo_dwg)