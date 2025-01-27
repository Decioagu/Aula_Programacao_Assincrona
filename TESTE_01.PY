from setuptools import setup

setup(
    name='meu_pacote',
    version='0.1',
    packages=['meu_pacote'],
    install_requires=['numpy', 'pandas'],  # Dependências
    entry_points={
        'console_scripts': [
            'meu_script=meu_pacote.meu_modulo:minha_funcao',
        ],
    },
)