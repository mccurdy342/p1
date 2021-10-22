#Objective: to add versions of color and print the assoicative name color
#input two colors and hex to name

#hex to rgb

#rgb to hex

#sum two hex

#sum tow rgb

hex_to_decimal = {'0':0, '1':1, '2':2, '3':3, '4':4 , '5':5, '6':6, '7':7, '8':8, '9':9 , 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

decimal_to_hex = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D',14:'E', 15:'F'}

def add_two_hex(hex1, hex2):
    dec1 = hex_to_decimal[hex1]
    dec2 = hex_to_decimal[hex2]

    sum = dec1 + dec2


def recursive_hex(hex, current_total):
    if  original_digit / 16 >= 1:
        current_total = current_total % 15
        hex = hex + "F"
        recursive_hex(hex, current_total)
    else:
        hex = hex
