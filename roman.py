def checkio(data):
    values = [1000, 500, 100, 50, 10, 5, 1]
    letters = ["M", "D", "C", "L", "X", "V", "I"]
    result = ""
    i = 0
    while True:
        if str(data)[0] == "9":
            if data >= 900:
                data -= 900
                result = result + "CM"
            elif data >= 90:
                data -= 90
                result = result + "XC"
            elif data >= 9:
                data -= 9
                result = result + "IX"
        elif data >= values[i]:
            data -= values[i]
            result = result + letters[i]
        elif i<len(values)-1:
            i += 1
        else:
            break
print(checkio(3999))