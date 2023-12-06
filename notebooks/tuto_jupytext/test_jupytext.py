# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Instalación de Jupytext
```bash
$ pip install jupytext
```

# Podemos marcar con qué tipo de documentos queremos emparejarlo:
# En este caso lo hemos emparejado con:
#
# - .py
# - .md
#
# De esta forma podemos excluir los archivos .ipynb de git, y trabajar con archivos de texto plano
#
# ![image.png](attachment:7a96bce1-3a18-4dc4-9293-795bcd9987fb.png)

# # Instalamos librerías

import pandas as pd
from random import sample

# # Creamos dataframe

df = pd.DataFrame({'a': sample(range(-100, 100), 50), 'b':sample(range(-100, 100), 50)})

# # Lo ploteamos

df.plot.scatter(x='a', y='b')

# ## Pandoc

# Con pandoc podemos mover nuestro trabajo a distintos tipos de txt
#
# https://pandoc.org/
#
#
# Instalamos pandoc y finalmente escribimos este comando:
#
# ```
# pandoc -o output.docx -f markdown -t docx .\test_jupytext.md
# ```
#
# El resultado:
#
# ![image.png](attachment:733f3a1f-d6ae-4e4c-9a8d-4d8c9a7e3a2c.png)


