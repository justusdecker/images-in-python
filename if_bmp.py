


def loader(file_name: str):
    # BitMap File Header
    # DIB Header
    assert file_name.endswith('.bmp')
    with open(file_name, 'rb') as file:
        image = file.read()
    
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