def mon_lan(text):
    while True:
        new_text = text.replace("ANA","A").replace("BAS","A")

        if text == new_text:
            break
        else:
            text = new_text

    if text == "A":
        return True

    else:
        return False
while True:
    word = input()
    if word == "X":
        break
    if mon_lan(word):
        print("YES")
    else:
        print("NO")