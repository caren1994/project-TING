
def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        news = instance.search(i)
        info = {
            "palavra": word,
            "arquivo": news["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for j, line in enumerate(news["linhas_do_arquivo"], 1):
            if word.lower() in line.lower():
                info["ocorrencias"].append({"linha": j})
        if info["ocorrencias"]:
            result.append(info)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
