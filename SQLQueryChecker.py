import sqlfluff


class SQLQueryChecker:
    def __init__(self):
        pass

    @staticmethod
    def check_sql_syntax(sql_query):
        """
        Verifica la sintaxis de una consulta SQL utilizando sqlfluff.

        Args:
            sql_query (str): La consulta SQL a verificar.

        Returns:
            dict: Resultados del linting de la consulta.
        """
        try:
            # Analizar la consulta SQL y obtener los resultados de linting
            result = sqlfluff.lint(sql_query, dialect="mysql")
            return result

        except Exception as e:
            print(f"Ocurrió un error: {e}")

    @staticmethod
    def obtener_codigos(json_data):
        """
        Obtiene los códigos de un conjunto de datos JSON.

        Args:
            json_data (list): Lista de diccionarios con claves 'code'.

        Returns:
            list: Lista de códigos extraídos.
        """
        codigos = [item['code'] for item in json_data]
        return codigos

    @staticmethod
    def obtener_codigo_y_descripcion(json_data):
        """
        Obtiene los pares (código, descripción) de un conjunto de datos JSON.

        Args:
            json_data (list): Lista de diccionarios con claves 'code' y 'description'.

        Returns:
            list: Lista de tuplas (código, descripción) extraídas.
        """
        codigo_y_descripcion = [(item['code'], item['description']) for item in json_data]
        return codigo_y_descripcion

    @staticmethod
    def corregir_errores(sql_query, dialect="mysql"):
        """
        Corrige errores en una consulta SQL dada.

        Args:
            sql_query (str): La consulta SQL a corregir.
            dialect (str): El dialecto SQL a utilizar. Por defecto, es "mysql".

        Returns:
            str: La consulta SQL corregida.
        """
        print("\nQuery inicial:")
        print(sql_query)
        print("\n")

        # Análisis de la query
        result = SQLQueryChecker.check_sql_syntax(sql_query)

        # Obtener los errores
        errores = SQLQueryChecker.obtener_codigo_y_descripcion(result)

        # Inicializar lista de errores a corregir
        errores_a_corregir = []

        while errores:
            print("Errores encontrados:")
            for i, (codigo, descripcion) in enumerate(errores, start=1):
                print(f"{i}. {codigo}: {descripcion}")
            print("\n")

            if errores_a_corregir == []:
                # Preguntar al usuario qué errores corregir
                respuesta = input(
                    "¿Cuáles errores deseas corregir? (Escribe 'all', 'none' o el número del error): ").lower()
            else:
                respuesta = input("¿Cuáles errores deseas corregir? ('none' o el número del error): ").lower()

            if respuesta == 'all' and errores_a_corregir == []:
                errores_a_corregir = errores
                break
            elif respuesta == 'none':
                break
            elif respuesta.isdigit():
                indice = int(respuesta) - 1
                if 0 <= indice < len(errores):
                    errores_a_corregir.append(errores[indice])
                    errores.pop(indice)
                    print(f"Error {errores_a_corregir[-1][0]} agregado a la lista de correcciones. \n")
                else:
                    print("Opción inválida. Por favor, selecciona un número válido.")
                    continue  # Vuelve al inicio del bucle para preguntar sobre otro error
            else:
                print("Opción inválida. Por favor, selecciona 'all', 'none' o el número del error.")
                continue  # Vuelve al inicio del bucle para preguntar sobre otro error

            # Si quedan errores en la lista
            if errores != []:
                # Preguntar si el usuario desea corregir otro error
                respuesta_otro_error = input("¿Quieres corregir otro error? (Y/n): ")
                if respuesta_otro_error == 'Y':
                    continue  # Vuelve al inicio del bucle para preguntar sobre otro error
                else:
                    break

        print(f"\nCorrigiendo errores: {errores_a_corregir}")
        # Corregir los errores seleccionados
        for codigo, descripcion in errores_a_corregir:
            sql_query = sqlfluff.fix(sql_query, dialect=dialect, rules=[codigo])

        return sql_query
