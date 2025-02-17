def make_statement(statement, decloration, lines = 1):


    middle = (f"{decloration * 3} {statement} {decloration * 3}")
    top_bottom = decloration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


make_statement("Programming is Fun!","=", 3)
print()
make_statement("s Still Fun!", "*", 2)
print()
make_statement("Emoji in Action", "🐍")
