import os

def main():
    #escribe tu código abajo de esta línea

    os.system("clear")    
    x=0.5

    print(f"{'X':^10}{'Y':^10}{'Z':^10}")
    print("====================================")

    while x <= 10:
        y = 3 * x ** 2 + 7 * x - 15
        z = y - 2 * x ** 2

        print(f"{x:10.2f}{y:10.2f}{z:10.2f}")

        x += 0.5

if __name__=='__main__':
    main()
