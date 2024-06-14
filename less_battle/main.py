point = str(input('путь: ')).lower()
def teg(point):
    vowels = 'swen'
    for char in point:
        if char not in vowels:
            return ['Error']
    x = input('x:')
    if not x.isdigit() or int(x) not in range(0, 101):
        print('error')
        exit()
    y = input('y:')
    if not y.isdigit() or int(y) not in range(0, 101):
        print('error')
        exit()
    x = int(x)
    y = int(y)
    for i in point:
        match i:
            case 's': y -= 1
            case 'n': y += 1
            case 'w': x -= 1
            case 'e': x += 1
    return(x, y)
print(teg(point))




