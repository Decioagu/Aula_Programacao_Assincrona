from setuptools import setup
from Cython.Build import cythonize


setup( ext_modules=cythonize(['cumprimenta.pyx']))

# Ativa um ambiente virtual: .\venv\Scripts\activate
# Caminho: cd Modulo_04_Cython_01
# Terminal: python setup.py build_ext --inplace