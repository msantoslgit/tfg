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
# ## Comprovación del selector de DB

# %%
import sys 
from pprint import pprint
pprint(sys.path)
from pathlib import Path 
Path().absolute()

# %%
import sys
path_to_tfg = Path().absolute().parent.parent
print(path_to_tfg)
sys.path.insert(0, str(path_to_tfg))

# %%
from database_functions import get_available_db_directories

selected_db_directory = get_available_db_directories()
print(f"Directorio seleccionado: {selected_db_directory}")

# %%
