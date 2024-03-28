import os


class Tester:
    def __init__(self, openai_chat):
        self.openai_chat = openai_chat

    def test(self, test_file):
        print(f"Testing {test_file}...")

    import os

    def get_available_test_files(self):
        # Obtén la ruta del directorio actual del script
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Construye la ruta al directorio un nivel por encima
        parent_directory = os.path.abspath(os.path.join(script_directory, ".."))

        # Construye la ruta al directorio que contiene los test
        choices_directory = os.path.join(parent_directory, "tfg", "source", "test")

        # Lista los archivos disponibles en el directorio
        available_files = [f for f in os.listdir(choices_directory) if
                           os.path.isfile(os.path.join(choices_directory, f))]

        # Muestra los archivos disponibles por pantalla
        print("Archivos disponibles:")
        for index, file in enumerate(available_files, start=1):
            print(f"{index}. {file}")

        # Pide al usuario que elija un archivo
        while True:
            try:
                selected_index = int(input("Selecciona un número correspondiente al archivo deseado: ")) - 1

                # Verifica si el número ingresado es válido
                if 0 <= selected_index < len(available_files):
                    # Si el número es válido, salimos del bucle
                    break
                else:
                    print("Por favor, ingresa un número dentro del rango.")
            except ValueError:
                print("Por favor, ingresa un número entero.")

        # Retorna la ruta del archivo seleccionado
        selected_file = os.path.join(choices_directory, available_files[selected_index])

        return selected_file
