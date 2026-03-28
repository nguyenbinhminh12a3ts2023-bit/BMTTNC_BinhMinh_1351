import struct

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476
    
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')
    
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        
        a0, b0, c0, d0 = a, b, c, d
        
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
                s = [7, 12, 17, 22][j % 4]
                k = int(abs(__import__('math').sin(j + 1)) * 2**32)
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
                s = [5, 9, 14, 20][j % 4]
                k = int(abs(__import__('math').sin(j + 1)) * 2**32)
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
                s = [4, 11, 16, 23][j % 4]
                k = int(abs(__import__('math').sin(j + 1)) * 2**32)
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16
                s = [6, 10, 15, 21][j % 4]
                k = int(abs(__import__('math').sin(j + 1)) * 2**32)
            
            f = (f + a + k + words[g]) & 0xFFFFFFFF
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, s)) & 0xFFFFFFFF
        
        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF
    
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm MD5: ")
    print(md5(input_string.encode('utf-8')))