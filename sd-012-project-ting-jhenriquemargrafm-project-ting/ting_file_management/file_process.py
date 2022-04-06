import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    rows = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(rows),
        "linhas_do_arquivo": rows
    }

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(result)
    print(result)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(f'{result}', file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
