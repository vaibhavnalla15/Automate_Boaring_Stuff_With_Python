def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception ("Symbol must be a single character string.")
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    box_print('*', 20, 5)
    box_print('O', 20, 5)
    box_print('x', 0, 5)
    box_print('Zz', 20, 5)
except Exception as err:
    print(f"An exception happened: {str(err)}")
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print(f"An exception happened: {str(err)}")
