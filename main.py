from controller.controllerObradeArte import ArtController
from view.art_view import ArtView

def main():
    controller = ArtController()
    view = ArtView()

    while True:
        print("\nOpciones:")
        print("1. Agregar Pintura")
        print("2. Agregar Escultura")
        print("3. Ver obra de arte por nombre")
        print("4. Ver obras de arte por tipo")
        print("5. Actualizar estado de venta")
        print("6. Eliminar obra de arte por nombre")
        print("7. Ver todas las obras de arte")
        print("8. Salir")

        option = view.prompt_for_input("Seleccione una opción (1-8): ")

        if option == "1":
            nombre = view.prompt_for_input("Nombre de la pintura: ")
            autor = view.prompt_for_input("Autor: ")
            en_venta = view.prompt_for_input("¿Está en venta? (Si/No): ").lower() == 'true'
            dimensiones = view.prompt_for_input("Dimensiones: ")
            tecnica = view.prompt_for_input("Técnica: ")
            retrato = view.prompt_for_input("¿Es un retrato? (Si/No): ").lower() == 'true'
            resultado = controller.add_pintura(nombre, autor, en_venta, dimensiones, tecnica, retrato)
            view.display_message(f"Pintura agregada: {resultado}")

        elif option == "2":
            nombre = view.prompt_for_input("Nombre de la escultura: ")
            autor = view.prompt_for_input("Autor: ")
            en_venta = view.prompt_for_input("¿Está en venta? (Si/No): ").lower() == 'true'
            volumen = view.prompt_for_input("Volumen: ")
            material = view.prompt_for_input("Material: ")
            resultado = controller.add_escultura(nombre, autor, en_venta, volumen, material)
            view.display_message(f"Escultura agregada: {resultado}")

        elif option == "3":
            name = view.prompt_for_input("Nombre de la obra: ")
            artwork = controller.get_artwork_by_name(name)
            view.display_artwork(artwork)

        elif option == "4":
            type_of_art = view.prompt_for_input("Tipo de obra (Pintura/Escultura): ")
            artwork = controller.get_artwork_by_type(type_of_art)
            if isinstance(artwork, list) and not artwork:
                view.display_message("No se encontró ninguna obra de arte de este tipo.")
            else:
                for art in artwork:
                    view.display_artwork(art)

        elif option == "5":
            name = view.prompt_for_input("Nombre de la obra: ")
            en_venta = view.prompt_for_input("¿Está en venta? (True/False): ").lower() == 'true'
            resultado = controller.update_en_venta(name, en_venta)
            view.display_message(resultado)

        elif option == "6":
            name = view.prompt_for_input("Nombre de la obra a eliminar: ")
            resultado = controller.delete_artwork_by_name(name)
            view.display_message(resultado)

        elif option == "7":
            artworks = controller.all_view_artwork()
            if not artworks:
                view.display_message("No hay obras de arte para mostrar.")
            else:
                for artwork in artworks:
                    view.display_artwork(artwork)

        elif option == "8":
            view.display_message("Saliendo del programa.")
            break

        else:
            view.display_message("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
