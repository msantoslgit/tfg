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
# ## Set up del path para Jupyter

# %%
from pprint import pprint
#pprint(sys.path)
from pathlib import Path 
Path().absolute()

import sys
path_to_tfg = Path().absolute().parent.parent
# print(path_to_tfg)
sys.path.insert(0, str(path_to_tfg))


# %% [markdown]
# ## Import de la clase TokenPricing

# %%
from TokenPricing import TokenPricing


# %% [markdown]
# ## Ejemplo de uso 

# %%
# Uso de la clase
max_tokens = 50
price_per_token = 0.002 / 1000
model_name = "gpt-3.5-turbo"

token_pricing = TokenPricing(max_tokens, price_per_token, model_name)

# Ejemplo de uso de las funciones
text_string = "Hola, crees que Elisa es una chica guapa"


num_tokens = token_pricing.num_tokens_from_string(text_string)
total_price = token_pricing.total_price(num_tokens)

print(f"Number of tokens: {num_tokens}")
print(f"Total price: ${total_price}")

# %%
