h_shoots = 0
shoots = 0
while True:
    user_input = input("Head or Tail or Exit: ").strip()
    user_input.capitalize()
    with open("head_or_tail.txt", 'r') as file:
        headOrTail = file.readlines()
    if user_input.lower() != "exit":
        if user_input.lower() == "head":
            h_shoots += 1
        shoots += 1
        result = (h_shoots / shoots) * 100
        print(f"Heads : {result}%")
        headOrTail.append(user_input + '\n')

    with open("head_or_tail.txt", 'w') as file:
        file.writelines(headOrTail)

    if user_input.lower() == "exit":
        with open("head_or_tail.txt", 'r') as file:
            headOrTail = file.readlines()
        for index, item in enumerate(headOrTail):
            item = f"{index + 1}) {item}"
        with open("head_or_tail.txt", 'w') as file:
            file.writelines("")
        break
