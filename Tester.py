import os
import json
from Logger import Logger
from datetime import datetime


class Tester:
    def __init__(self, openai_chat):
        self.openai_chat = openai_chat
        self.test_file = self.get_available_test_files()
        self.log_file = self.generate_log_file(self.test_file)

        self.logger = Logger(self.log_file)

    def test(self):

        try:
            with open(self.test_file, 'r') as file:
                data = json.load(file)
                preguntas_respuestas = data.get("preguntas_respuestas", [])
                for pregunta_respuesta in preguntas_respuestas:
                    pregunta = pregunta_respuesta.get("pregunta", "")
                    respuesta_esperada = pregunta_respuesta.get("respuesta", "")
                    dificultad = pregunta_respuesta.get("dificultad", "")

                    # Loguea las variables
                    self.logger.write_log(f"Dificultad: {dificultad}")
                    self.logger.write_log(f"Pregunta: {pregunta}")
                    self.logger.write_log(f"Respuesta Esperada: {respuesta_esperada}")


                    response, query_corrected = self.openai_chat.handle_responses_window(pregunta)
                    self.logger.write_log(f"IA Response: {query_corrected}")

        except FileNotFoundError:
            print(f"El archivo {self.test_file } no existe.")

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



    def generate_log_file(self, test_file):
        # Obtener la ruta del directorio y el nombre del archivo
        directorio, nombre_archivo = os.path.split(test_file)

        # Obtener la fecha actual en el formato deseado
        # fecha_actual = datetime.now().strftime('%d_%m_%Y')
        fecha_actual = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')

        # Agregar la fecha al nombre del archivo
        nuevo_nombre_archivo = f"{fecha_actual}_{nombre_archivo}"

        # Combinar el directorio del log con el nuevo nombre del archivo
        nueva_ruta = os.path.join(directorio.replace('test', 'log'), nuevo_nombre_archivo)

        print(nueva_ruta)

        nueva_ruta = self.cambiar_extension(nueva_ruta)

        print(nueva_ruta)

        return nueva_ruta

    def cambiar_extension(self, path):
        # Obtener el directorio y el nombre del archivo sin la extensión
        directorio, nombre_archivo = os.path.split(path)
        nombre_base, _ = os.path.splitext(nombre_archivo)

        # Construir el nuevo path con la extensión cambiada
        nuevo_path = os.path.join(directorio, nombre_base + '.txt')
        return nuevo_path
