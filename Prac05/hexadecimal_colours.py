hex_colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd", "blue1":
               "#0000ff", "BlueViolet": "#8a2be2"}
for key in hex_colours:
    print(key)
get_input = input("Enter a name from the list to find the hexadecimal code: ")
if get_input in hex_colours:
    print(hex_colours[get_input])

