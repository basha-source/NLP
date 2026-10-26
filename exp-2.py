def accepts(text):
    state = 0

    for ch in text:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'a':
                state = 1
            elif ch == 'b':
                state = 2
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


text = input("Enter a string: ")

if accepts(text):
    print("String accepted")
else:
    print("String rejected")
