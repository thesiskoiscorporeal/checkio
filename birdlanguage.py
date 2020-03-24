VOWELS = "aeiouy"

def translate(phrase):
    output = ""
    i = 0
    
    while True:
        if i > len(phrase)-1:
            break
        elif phrase[i] in VOWELS:
            output += phrase[i]
            i += 3
        elif phrase[i] == " ":
            output += phrase[i]
            i += 1
        elif phrase[i] not in VOWELS:
            output += phrase[i]
            i += 2

    
    return output

print(translate("hoooowe yyyooouuu duoooiiine"))