
def better_byte_viewer(data: bytes) -> None:
    pr_string = ""
    
    left, right = [], []
    
    for index, byte in enumerate(data):
        char = chr(byte)
            
        pr_string += f"{char if char.isprintable() else '.'}"
        if (index + 1) % 16 == 0 and pr_string:
            right.append(pr_string)
            pr_string = ""
    else:
        if pr_string:

            right.append(pr_string)
            pr_string = ""
            
    for index, byte in enumerate(data):
        
        if byte < 16:
            num = f'0{hex(byte)[2:].upper()}'
        else:
            num = f'{hex(byte)[2:].upper()}'
        pr_string += f"{num} "
        if (index + 1) % 16 == 0 and pr_string:
            left.append(pr_string)
            pr_string = ""
    else:
        if pr_string:
            left.append(pr_string)
    
    for l,r in zip(left,right):
        print(f"{l:<48}{r}")

def colored_char(c: str, col: tuple[int]):
    r,g,b = col
    return f"\033[38;2;{r};{g};{b}m{c}\033[39m"

def loader(file_name: str):
    """
    low weight bmp loader. Will be not work in some cases
    """
    assert file_name.endswith('.bmp')
    with open(file_name, 'rb') as file:
        image = file.read()
    better_byte_viewer(image)

    data_offset = image[10:14]
    data_offset = int.from_bytes(data_offset,'little')
    
    width = image[18:22]
    height = image[22:26]
    bits_per_pixel = image[28:30]

    color_data = list(image[data_offset:])
    
    bpp = int.from_bytes(bits_per_pixel)
    w = int.from_bytes(width,'little')
    row_size = ((bpp * w + 31) // 32) * 4
    h = int.from_bytes(height,'little')
    
    padding = row_size - ((bpp * w) // 8)
    pixel_data = []
    for _ in range(h):
        row = []
        for _ in range(w):
            r = color_data.pop(0)
            g = color_data.pop(0)
            b = color_data.pop(0)
            row.append((b,g,r))
        pixel_data.append(row)
        for i in range(padding):
            color_data.pop(0)
    print(pixel_data)
    for x in pixel_data:
        for y in x:
            print(colored_char("X",y),end='')
        print()
    assert int.from_bytes(width,"little") == 8 and int.from_bytes(height,"little") == 16
    
    
    pass
loader('test.bmp')