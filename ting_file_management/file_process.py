from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return False

    content = txt_importer(path_file)

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }
    instance.enqueue(info)
    sys.stdout.write(str(info))


def remove(instance):
    if not len(instance) > 0:
        return sys.stdout.write("Não há elementos\n")
    file_removed = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {file_removed} removido com sucesso\n")


def file_metadata(instance, position):
    if position < 0 or position > len(instance) - 1:
        sys.stderr.write("Posição inválida")
    else:
        file = instance.search(position)
        sys.stdout.write(str(file))
