import sys
from os import path


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)
    if not path.exists(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    with open(path_file, "r") as file:
        rows = file.read()
        return rows.split('\n')
