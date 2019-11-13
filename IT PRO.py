def get_init_data():
    
    def get_data():
        digit = None
        print('Введите число:')
        while digit is None:
            try:
                digit = float(input())
            except ValueError:
                print('Введите число заново: ')
        return digit
    
    print('Вводим коэффициент a')
    a = get_data()
    print('Вводим коэффициент b')
    b = get_data()
    print('Вводим коэффициент c')
    c = get_data()
    return a, b, c

