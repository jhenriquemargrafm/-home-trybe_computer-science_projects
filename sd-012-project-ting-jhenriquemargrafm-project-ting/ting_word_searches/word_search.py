def exists_word(word, instance):
    word_log = list()

    for index in range(len(instance)):
        file = instance.search(index)
        occurrence = list()

        for row, sentence in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in sentence.lower():
                occurrence.append({"linha": (row + 1)})

        if len(occurrence) > 0:
            word_log.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                }
            )

    return word_log


def search_by_word(word, instance):
    log_content = list()

    for index in range(len(instance)):
        file = instance.search(index)
        occurrence = list()

        for row, sentence in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in sentence.lower():
                occurrence.append({
                    "linha": (row + 1),
                    "conteudo": sentence
                })

        if len(occurrence) > 0:
            log_content.append(
                {
                  "palavra": word,
                  "arquivo": file["nome_do_arquivo"],
                  "ocorrencias": occurrence
                }
            )

    return log_content
