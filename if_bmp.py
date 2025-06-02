
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

def bit_viewer(data: bytes):
    pr_string = ""
    for index, byte in enumerate(data):
        char = chr(byte)
            
        pr_string += f"{char if char.isprintable() else '.'}"
        if index % 16 == 0 and pr_string:
            print(pr_string)
            pr_string = ""
    else:
        if pr_string:
            print(pr_string)
    pr_string = ""
    for index, byte in enumerate(data):
        
        if byte < 16:
            num = f'0{hex(byte)[2:].upper()}'
        else:
            num = f'{hex(byte)[2:].upper()}'
        pr_string += f"{num} "
        if (index + 1) % 16 == 0 and pr_string:
            print(pr_string)
            pr_string = ""
    else:
        if pr_string:
            print(pr_string)

def loader(file_name: str):
    # BitMap File Header
    # DIB Header
    assert file_name.endswith('.bmp')
    with open(file_name, 'rb') as file:
        image = file.read()
    better_byte_viewer(image)
    # Header
    
    signature = image[:2]
    file_size = image[2:6]
    reserved = image[6:10] #! unused
    data_offset = image[10:14]
    
    # InfoHeader
    
    size = image[14:18]
    width = image[18:22]
    height = image[22:26]
    planes = image[26:28]
    bits_per_pixel = image[28:30]
    compression = image[30:34]
    image_size = image[34:38]
    x_pixels_per_m = image[38:42]
    y_pixels_per_m = image[42:46]
    colors_used = image[46:50]
    important_colors = image[50:54]
    
    #Color Table
    
    


    assert int.from_bytes(width,"little") == 8 and int.from_bytes(height,"little") == 16
    
    
    pass
loader('test.bmp')