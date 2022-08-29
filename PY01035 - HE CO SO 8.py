def process():
    print(oct(int(input(), 2))[2:])

def main():
    t = 1
    while t > 0:
        process()
        t -= 1
        
if __name__ == '__main__':
    main()