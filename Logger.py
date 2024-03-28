import logging
class Logger:
    def __init__(self, file_path, level=logging.INFO, format='%(message)s'):
        self.file_path = file_path
        self.level = level
        self.format = format

        # Configurar el registro
        logging.basicConfig(filename=self.file_path, level=self.level, format=self.format)

    def write_log(self, message):
        logging.info(message)
