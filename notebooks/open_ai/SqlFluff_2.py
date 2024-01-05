# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ### Importamos sqlfluff

# %%
import sqlfluff


# %%
def check_sql_syntax(sql_query):
    try:
        # Analizar la consulta SQL y obtener los resultados de linting
        result = sqlfluff.lint(sql_query, dialect="mysql")

        return result
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")



# %%
# Consulta SQL de ejemplo
sql_query_example = "SELECT nombre_centro FROM Centros WHERE id_centro = 3"

# %%
# Verificar la sintaxis de la consulta
check_sql_syntax(sql_query_example)

# %%
result = check_sql_syntax(sql_query_example)

# %%
print(result)


# %%

# %%

# %%

# %%
def obtener_codigos(json_data):
    codigos = [item['code'] for item in json_data]
    return codigos


# %%
array_codigos = obtener_codigos(result)
print(array_codigos)


# %%
def obtener_codigo_y_descripcion(json_data):
    codigo_y_descripcion = [(item['code'], item['description']) for item in json_data]
    return codigo_y_descripcion


# %%
tupla_codigo_descripcion = obtener_codigo_y_descripcion(result)
print(tupla_codigo_descripcion)


# %%

# %%

# %%
def corregir_errores(sql_query, dialect="mysql"):

    print("\nQuery inicial:")
    print(sql_query)
    print("\n")

    # Análisis de la query
    result = check_sql_syntax(sql_query_example)
    
    # Obtener los errores
    errores = obtener_codigo_y_descripcion(result)
    
    # Inicializar lista de errores a corregir
    errores_a_corregir = []

    while errores:
        print("Errores encontrados:")
        for i, (codigo, descripcion) in enumerate(errores, start=1):
            print(f"{i}. {codigo}: {descripcion}")
        print("\n")

        if errores_a_corregir == []:
            # Preguntar al usuario qué errores corregir
            respuesta = input("¿Cuáles errores deseas corregir? (Escribe 'all', 'none' o el número del error): ").lower()
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


# %%
# Ejemplo de uso:
sql_query_ejemplo = "SELECT nombre_centro FROM Centros WHERE id_centro = 3"
sql_query_corregido = corregir_errores(sql_query_ejemplo, dialect="mysql")

print("\nQuery final:")
print(sql_query_corregido)

# %%
