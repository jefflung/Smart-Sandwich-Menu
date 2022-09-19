def smartSandwich():
    ask_order = input("Which sandwich would you like? ")
    low_ask = ask_order.lower()
    
    with open("menu.txt", mode="r") as menu:
        found = False
        for line in menu:
            #remove space between words to check the line includes word or not
            if low_ask.strip() in line.lower().strip():
                print("Below sandwich includes the gradient",ask_order,":\n",line.strip())
                #only matched item in menu showing Yes answer
                found = True
        if not found:
            print("Sorry, we don't have",low_ask,"sandwich in our menu.")
                
smartSandwich()
