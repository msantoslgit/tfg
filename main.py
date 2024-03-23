import tkinter as tk
from openai import OpenAI
from OpenAIChat import OpenAIChat
from database_functions import get_available_db_directories, read_db_txt
from component import API_KEY, init_prompt


class ChatInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OpenAI Chat Interface")

        # Inicialización de variables globales
        self.client = OpenAI(api_key=API_KEY)
        self.model = "gpt-3.5-turbo"
        self.max_tokens = 200
        self.price_per_token = 0.002 / 1000

        # Cargar el contenido de la base de datos
        self.selected_db_directory = get_available_db_directories()
        self.db_content = read_db_txt(self.selected_db_directory)

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

        self.send_button = tk.Button(self, text="Enviar", command=self.send_message)
        self.send_button.pack()

        # Inicializar la interfaz
        self.update_output("Initial loading of the database has succeeded. Now you can ask anything related to the model\n"
                           "Enter 'exit' to close the current session or 'reset' to reload the DB and restart the chat\n"
                           "Enter 'cost' to know how much is the actual cost in dollars for all the request to the API\n")

    def send_message(self):
        content = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        if content == "exit":
            self.openai_chat.close_session()
            self.destroy()

        elif content == "reset":
            response = self.openai_chat.reset_session([{"role": "system", "content": init_prompt}], self.db_content)
            if response == '1':
                self.update_output("Reset session successfully\n")
            else:
                self.update_output("Failed trying to reset the OpenAIChat\n")

        elif content == "cost":
            cost_message = f"Actual cost in dollars: {self.openai_chat.get_total_cost():.2f}\n"
            self.update_output(cost_message)

        else:
            # response = self.openai_chat.get_response(content)
            response = 'Respuesta ejemplo api'
            self.update_output(response + "\n")

    def update_output(self, text):
        # Limpiar el contenido existente
        self.output_text.delete(1.0, tk.END)
        # Insertar el nuevo texto
        self.output_text.insert(tk.END, text)
        # Asegurarse de que la nueva entrada sea visible
        self.output_text.see(tk.END)


if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()
