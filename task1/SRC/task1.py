def mathConverter(n, style):
    if style > 36 or style < 2:
        return "usage"
    
    mathConverter.t = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'           
    r = ''
    while n:
        n, y = divmod(n, style) 
        r = mathConverter.t[y] + r
    return r

def main():
    print(mathConverter(364542, 0))
    print(mathConverter(364542, 2))
    print(mathConverter(364542, 8))
    print(mathConverter(364542, 16))
    print(mathConverter(364542, 37))

if __name__ == '__main__':
    main()
