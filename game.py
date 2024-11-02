def user_option():
    options = ["Rock", "Paper", "scissors"]
    for i,option in enumarate(options):
        print(f"{i}:{option}")


    while true:
        try:
            user = input(int(f"Introduce the number between (1-3): "))
        except ValueError:
