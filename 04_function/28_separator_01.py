def separator(char, repeat):
    """print any char for any times in a single line"""
    print(char * repeat)


def separator2(char, repeat, lines):
    """print any char for any times and any lines

    :param char: the char we use for separator
    :param repeat: how many chars we want
    :param lines: how many lines we want
    """
    i = 0
    while i < lines:
        separator("-", 30)
        i = i + 1


# separator("*", 50)

separator2("-", 50, 3)
