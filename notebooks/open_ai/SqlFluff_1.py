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


# %% [markdown]
# ### Definimos una primera función que obtiene los errores de la query
# - Devuelve un array con los errores de la query
# - Si no hay errores de ningún tipo devuelve el array vacío
# - Lo bueno que tenemos es que devuelve los códigos de los errores dentro del array para identificarlos 

# %%
def check_sql_syntax(sql_query):
    try:
        # Analizar la consulta SQL y obtener los resultados de linting
        result = sqlfluff.lint(sql_query, dialect="mysql")

        # Verificar si hay errores
        if result == []:
            print("La sintaxis de la consulta es válida.")
        else:
            print("La sintaxis de la consulta contiene errores:")
            for error in result:
                print(error)
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")



# %% [markdown]
# ### Definimos una query de ejemplo  

# %%
# Consulta SQL de ejemplo
sql_query_example = "SELECT nombre_centro FROM Centros WHERE id_centro = 3"

# %% [markdown]
# ### Detección de errores

# %%
# Verificar la sintaxis de la consulta
check_sql_syntax(sql_query_example)

# %% [markdown]
# ### Corrección de errores

# %%
sqlfluff.fix(sql_query_example, dialect="mysql")

# %%

# %% [markdown]
# ### Definimos un segundo ejemplo 

# %%
sql_query_example = "SELECT nombre_producto, precio FROM Productos ORDER BY precio DESC LIMIT 1;\n"

# %%
# Verificar la sintaxis de la consulta
check_sql_syntax(sql_query_example)

# %%
sqlfluff.fix(sql_query_example, dialect="mysql")

# %%

# %% [markdown]
# ### Corrección por trozos 

# %%
### Aquí vamos a probar que se pueden corregir solo ciertos errores que pasamos por parámetro a la fucnión 

# %%
sql_query_example = "SELECT nombre_producto, precio FROM Productos ORDER BY precio DESC LIMIT 1;\n"

# %%
# Verificar la sintaxis de la consulta
check_sql_syntax(sql_query_example)

# %%
# We can also fix just specific rules.
fix_result_2 = sqlfluff.fix(sql_query_example, dialect="mysql", rules=["LT09"])
print(fix_result_2)

# %% [markdown]
# - En la respuesta superior podemos ver que ha añadido los saltos de línea corrigiendo el LT09

# %%
# Or a subset of rules...
fix_result_3 = sqlfluff.fix(sql_query_example, dialect="mysql", rules=["CP02"])
print(fix_result_3)

# %% [markdown]
# - En la respuesta superior podemos ver que corregido el uso de mayusculas con el CP02

# %%
