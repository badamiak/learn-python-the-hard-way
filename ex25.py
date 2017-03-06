def break_words(stuff: str) -> list:
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words: list) -> list:
    """this one will sort the words/"""
    return sorted(words)

def print_first_word(words: list) -> None:
    "prints first word after popping it off."
    word = words.pop(0)
    print(word)

def print_last_word(words: list) -> None:
    """prints last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence: str) -> list:
    """takes full sentence and returns sorted words."""
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence: str) -> None:
    """Prints the first and the last words of the sentence."""
    words = break_words(sentence)
    print_firs_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence: str) -> None:
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_firs_word(words)
    print_last_word(words)

print("done")