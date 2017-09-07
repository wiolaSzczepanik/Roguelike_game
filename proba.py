def import_highscore(filename):
    highscore = {}
    with open(filename) as text:
        text = list(text)
        text_list = []
        for element in text:
            text_list.append(element.strip("\n").split("|"))

        for line in text_list:
            highscore[line[0]] = float(line[1])

        return highscore
