def tong(a, b):
    res = a + b
    return res

def hello(name1, name2, name3):
    print("Xin chào", name1, name2, name3)

if __name__ == '__main__':
    c, d = map(int, input().split())
    print(tong(c ,d))
    hello('a', 'b', 'c')