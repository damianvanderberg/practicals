# hex colour code identifier


hex_colour_dict = {"AliceBlue": "#f0f8ff", "aquamarine4": "#458b74", "black": "#000000", "BlanchedAlmond": "#ffebcd",
                   "BlueViolet": "#8a2be2", "CadetBlue": "#5f9ea0", "chocolate": "	#d2691e",
                   "CornflowerBlue": "#6495ed",
                   "DarkGoldenrod": "#b8860b", "DarkKhaki": "#bdb76b"}

colour_name = input("Enter a colour name: ")

while colour_name != "":
    print("The code for {} is {}".format(colour_name, hex_colour_dict.get(colour_name)))

    colour_name = input("Enter a colour name: ")
