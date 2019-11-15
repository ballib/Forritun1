with open("words.txt", "r", encoding="utf-8") as rf:
    for line in rf:
        replace = line.replace('. ', '.\n')
        stripped = replace.strip()
        print(stripped, end=" ")

    with open("sentences.txt", "w") as w:
        w.write(stripped)