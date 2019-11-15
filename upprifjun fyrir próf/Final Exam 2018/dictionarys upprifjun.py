my_dict = {}

chess_dict = {"carlsen": 2876}

print(chess_dict)

chess_dict["anand"] = 2765

print(chess_dict)

print(chess_dict["anand"])
chess_dict["caruana"] = 2812

print(chess_dict)
if "anand" in chess_dict:
    print(True)