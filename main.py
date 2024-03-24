import os
import tkinter as tk
from openai import OpenAI
from OpenAIChat import OpenAIChat
from database_functions import read_db_txt_window
from component import API_KEY, init_prompt, init_database_message, instructions
from tkinter import Listbox, Scrollbar, END, VERTICAL, Y


class DirectorySelectionWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Seleccionar Directorio")

        # Obtener el directorio de la base de datos disponible
        self.get_available_db_directories()

    def get_available_db_directories(self):
        selected_directory = None

        def on_select():
            nonlocal selected_directory
            selection = listbox.curselection()
            if selection:
                selected_index = selection[0]
                selected_directory = os.path.join(choices_directory, available_directories[selected_index])
                self.parent.directory_selection = selected_directory
                self.destroy()  # Cerrar la ventana de selección


        script_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.abspath(os.path.join(script_directory, ".."))
        choices_directory = os.path.join(parent_directory, "tfg", "source", "DB")
        available_directories = [d for d in os.listdir(choices_directory) if
                                 os.path.isdir(os.path.join(choices_directory, d))]

        listbox = Listbox(self, selectmode=tk.SINGLE)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for directory in available_directories:
            listbox.insert(END, directory)

        scrollbar = Scrollbar(self, orient=VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=Y)
        listbox.config(yscrollcommand=scrollbar.set)

        select_button = tk.Button(self, text="Seleccionar", command=on_select)
        select_button.pack()


class ChatInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OpenAI Chat Interface")

        # Inicialización de variables globales
        self.client = OpenAI(api_key=API_KEY)
        self.model = "gpt-3.5-turbo"
        self.max_tokens = 200
        self.price_per_token = 0.002 / 1000
        self.directory_selection = None

        # Abrir la ventana de selección del directorio de la base de datos
        self.directory_selection_window = DirectorySelectionWindow(self)
        self.wait_window(self.directory_selection_window)

        # Cargar el contenido de la base de datos seleccionada
        db_reader_output, self.db_content = read_db_txt_window(self.directory_selection)

        # Iniciar la conversación con un mensaje del sistema
        self.init_conversation = [{"role": "system", "content": init_prompt}]

        # Inicializar la clase OpenAIChat
        self.openai_chat = OpenAIChat(api_key=API_KEY, conversation=self.init_conversation,
                                      model=self.model, max_tokens=self.max_tokens,
                                      price_per_token=self.price_per_token)

        # Crear elementos de la interfaz
        self.output_text = tk.Text(self, height=20, width=60)
        self.output_text.pack(expand=True, fill=tk.BOTH)  # Expandir tanto horizontal como verticalmente

        self.input_entry = tk.Entry(self, width=50)
        self.input_entry.pack(fill=tk.X)  # Expandir solo horizontalmente

        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)  # Alinea el botón a la izquierda

        self.instructions_button = tk.Button(self, text="Instructions", command=self.print_instructions)
        self.instructions_button.pack(side=tk.RIGHT)  # Alinea el botón a la derecha

        # Inicializar la interfaz
        self.update_output(
            db_reader_output
            + "\n" + "\n"
            + init_database_message)

    def send_message(self):
        content = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        if content == "Exit" or content == "exit":
            self.openai_chat.close_session()
            self.destroy()

        elif content == "Reset" or content == "reset":
            response = self.openai_chat.reset_session([{"role": "system", "content": init_prompt}], self.db_content)
            if response == '1':
                self.update_output("Reset session successfully\n")
            else:
                self.update_output("Failed trying to reset the OpenAIChat\n")

        elif content == "Cost" or content == "cost":
            cost_message = f"Actual cost in dollars: {self.openai_chat.get_total_cost():.7f}\n"
            self.update_output(cost_message)

        else:
            # response = self.openai_chat.get_response(content)
            # # response = 'Respuesta ejemplo api'
            # formatted_json_string = response.replace(', "', ',\n "')
            # self.update_output(formatted_json_string + "\n")

            response, query_corrected = self.openai_chat.handle_responses_window(content)
            # response = 'Respuesta ejemplo api'
            formatted_json_string = response.replace(', "', ',\n "') + "\n" +  "\n" + "The corrected query is: " + "\n" +  query_corrected
            self.update_output(formatted_json_string + "\n")

    def update_output(self, text):
        # Limpiar el contenido existente
        self.output_text.delete(1.0, tk.END)
        # Insertar el nuevo texto
        self.output_text.insert(tk.END, text)
        # Asegurarse de que la nueva entrada sea visible
        self.output_text.see(tk.END)

    def print_instructions(self):

        self.update_output(instructions)


if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()
