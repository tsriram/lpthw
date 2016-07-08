DIRECTIONS = ['north', 'south', 'east', 'west', 'up', 'left', 'right', 'back']

VERBS = ['go', 'stop', 'kill', 'eat']

STOP_WORDS = ['the', 'in', 'of', 'from', 'at', 'it']

NOUNS = ['door', 'bear', 'princess', 'cabinet']

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return False

def scan(input):
    words = input.split()
    sentence = []
    for word in words:
        number = convert_numbers(word)
        if number:
            sentence.append(('number', number))
        elif word in DIRECTIONS:
            sentence.append(('direction', word))
        elif word in VERBS:
            sentence.append(('verb', word))
        elif word in STOP_WORDS:
            sentence.append(('stop', word))
        elif word in NOUNS:
            sentence.append(('noun', word))
        else:
            sentence.append(('error', word))
    print sentence
    return sentence