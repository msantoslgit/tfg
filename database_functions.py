import os


def get_available_db_directories():
    # Obtén la ruta del directorio actual del script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta al directorio un nivel por encima
    parent_directory = os.path.abspath(os.path.join(script_directory, ".."))

    # Construye la ruta al directorio que contiene las carpetas a elegir
    choices_directory = os.path.join(parent_directory, "tfg", "source", "DB")

    # Lista los directorios disponibles en el nivel deseado
    available_directories = [d for d in os.listdir(choices_directory) if os.path.isdir(os.path.join(choices_directory, d))]

    # Muestra los directorios disponibles por pantalla
    print("Directorios disponibles:")
    for index, directory in enumerate(available_directories, start=1):
        print(f"{index}. {directory}" + '\n')

    # Pide al usuario que elija un directorio
    while True:
        try:
            selected_index = int(input("Selecciona un número correspondiente al directorio deseado: ")) - 1

            # Verifica si el número ingresado es válido
            if 0 <= selected_index < len(available_directories):
                # Si el número es válido, salimos del bucle
                break
            else:
                print("Por favor, ingresa un número dentro del rango." + '\n')
                print("Directorios disponibles:")
                for index, directory in enumerate(available_directories, start=1):
                    print(f"{index}. {directory}" + '\n')
        except ValueError:
            print("Por favor, ingresa un número entero." + '\n')
            print("Directorios disponibles:")
            for index, directory in enumerate(available_directories, start=1):
                print(f"{index}. {directory}" + '\n')

    # Construye la ruta completa al directorio seleccionado
    selected_directory = os.path.join(choices_directory, available_directories[selected_index])

    # Retorna la ruta del directorio seleccionado
    return selected_directory


def read_db_txt(directory_path):
    # Check if the path is valid
    if not os.path.isdir(directory_path):
        return "The provided path is not a valid directory."

    # Initialize the string to concatenate the content
    concatenated_content = ""

    print("List of files:")
    # Iterate through all files in the directory
    for file_name in os.listdir(directory_path):
        # Check if the file has a .txt extension
        if file_name.endswith(".txt"):

            print(file_name)
            # Build the full file path
            file_path = os.path.join(directory_path, file_name)

            # Read the content of the file and concatenate it to the string
            with open(file_path, 'r') as file:
                concatenated_content += file.read() + '\n' + '\n'

    print('\n')
    return concatenated_content
