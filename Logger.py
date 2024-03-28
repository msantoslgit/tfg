import logging

class Logger:
    def __init__(self, file_path, level=logging.INFO, format='%(message)s'):
        self.file_path = file_path
        self.level = level
        self.format = format

        # Crear un logger solo para esta instancia
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level)

        # Agregar un manejador de archivo con el formato especificado
        file_handler = logging.FileHandler(self.file_path)
        file_handler.setLevel(self.level)
        formatter = logging.Formatter(self.format)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def write_log(self, message):
        self.logger.info(message)
