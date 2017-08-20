# RGB HEX Converter

"""In this project, a calculator that can convert RGB values to Hexadecimal (hex) values, and vice-versa will be built with the bitwise operators.

We'll add three methods to the project:

A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle"""

# A method to convert RGB to Hex
def rgb_hex():
  invalid_msg = "Invalid values were entered!"
  red = int(raw_input("Enter the red value: "))
  if red < 0 or red > 255:
    print invalid_msg
  blue = int(raw_input("Enter the blue value: "))
  if blue < 0 or blue > 255:
    print invalid_msg
  green = int(raw_input("Enter the green value: "))
  if green < 0 or green > 255:
    print invalid_msg
      
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()

# A method to convert Hex to RGB
def hex_rgb():
  hex_val = raw_input("Enter a hexadecimal value: ")
  if len(hex_val) != 6:
    print "An invalid value was entered!"
  else:
    hex_val = int(hex_val, 16)
    
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  
  hex_val = hex_val >>8
  red = hex_val % two_hex_digits
  
  print "Red: %s Blue: %s Green: %s"%(red, blue, green)
  
# A method that starts a promp cycle
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB to Hex"
      rgb_hex()
    elif option == "2":
      print "Hex to RGB"
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "Error."

      
convert()
