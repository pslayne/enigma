import numpy as np

def get_max_size(shape):
    # 2 bits per pixel
    size = shape[0] * shape[1] * 2
    if(len(shape) >= 3):
        size *= shape[2]
    return size

def hide(img, cipher):
    max_size = get_max_size(img.shape)
    # raises value error if the image doesn't fit in the image 
    # or if the number characters is greater than the maximum number that can be represented in 32 bits
    if(len(cipher) > max_size or len(cipher) > int('11111111111111111111111111111111', 2)):
        raise ValueError("Message doesn't fit")

    stream = cipher_to_bin(cipher)
    if len(img.shape) >= 3:
        return hide_multi_channel(img, stream)
    else:
        return hide_single_channel(img, stream)

def cipher_to_bin(cipher):
    stream = ''
    for b in cipher:
        stream += bin(b)[2:].zfill(8)
    return stream

def hide_single_channel(img, stream):
    out_img = []
    i = 0
    for line in img:
        aux_line = []
        for pixel in line:
            bin_value = bin(pixel)[2:].zfill(8)
            
            if(i < len(stream)):
                bin_value = bin_value[:-2] + stream[i:i+2]
                i += 2

            aux_line.append(int(bin_value, 2))
            
        out_img.append(aux_line)
    out_img = np.array(out_img, dtype=np.uint8)
    return out_img

def hide_multi_channel(img, stream):
    out_img = []
    i = 0
    for line in img:
        aux_line = []
        for pixel in line:
            aux_pixel = []
            for ch in pixel:
                bin_value = bin(ch)[2:].zfill(8)
                
                if(i < len(stream)):
                    bin_value = bin_value[:-2] + stream[i:i+2]
                    i += 2

                aux_pixel.append(int(bin_value, 2))
            aux_line.append(aux_pixel)
        out_img.append(aux_line)
    out_img = np.array(out_img, dtype=np.uint8)
    return out_img

def reveal(img):
    # retrieves the cipher from the given img
    img = img.flatten()
    size = get_size(img)
    stream = ''
    for i in range(0, size*4):
        stream += bin(img[16+i])[2:].zfill(8)[6:]

    return int(stream, 2).to_bytes(size, 'big')

def get_size(img):
    # gets the size from the first 32 bits of the img
    stream = ''
    for i in range(16):
        stream += bin(img[i])[2:].zfill(8)[6:]
        
    return int(stream, 2)
