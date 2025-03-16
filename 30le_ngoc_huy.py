import math
from fractions import Fraction

# Ham nhap so nguyen duong
def get_positive_integer():
    while True:
        n = int(input("Nhap so nguyen duong n: "))
        if n > 0:
            return n
        print("Vui long nhap lai!")

# Bai 1: Tinh tong su dung vong lap while
def tinh_tong_bai_1():
    n = get_positive_integer()

    # a)
    S4 = 0
    i = 1
    while i <= n:
        S4 += i**2
        i += 1
    print("S4 =", S4)

    # b)
    S5 = 0
    i = 1
    while i <= (2*n + 1):
        S5 += i**3
        i += 2
    print("S5 =", S5)

    # c)
    S6 = 0
    i = 2
    while i <= (2*n):
        S6 += i**4
        i += 2
    print("S6 =", S6)

# Bai 2: 
def tinh_tong_bai_2():
    n = get_positive_integer()

    # a)
    S = 0
    i = 1
    while i <= n:
        S += (-1)**(i+1) * (1/i)
        i += 1
    print("S =", S)

    # b)
    S = 0
    i = 1
    while i <= n:
        S += i / (i + 1)
        i += 1
    print("S =", S)

    # c) 
    S = 0
    i = 2
    while i <= n + 1:
        S += 1 / math.sqrt(i)
        i += 1
    print("S =", S)

# Bai 3:
def cos_taylor(x, epsilon=1e-4):
    term = 1
    cos_x = 1
    n = 1
    while abs(term) > epsilon:
        term = (-1) ** n * (x ** (2 * n)) / math.factorial(2 * n)
        cos_x += term
        n += 1
    return cos_x

def tinh_cos():
    x = float(input("Nhap x (radian): "))
    print("cos(x) ≈", cos_taylor(x))

# Bai 4:
def nhap_phan_so():
    while True:
        tu_so = int(input("Nhap tu so: "))
        mau_so = int(input("Nhap mau so: "))
        if mau_so != 0:
            break
        print("Mau so khong duoc bang 0, vui long nhap lai!")

    phan_so = Fraction(tu_so, mau_so)
    print("Phan so sau khi toi gian:", phan_so)

# Bai 5:
def nhap_den_so_am():
    while True:
        num = int(input("Nhap mot so: "))
        if num < 0:
            print("Dung chuong trinh!")
            break

# Bai 6:
def so_sang_chu():
    num_to_words = {
        '0': "Khong", '1': "Mot", '2': "Hai", '3': "Ba", '4': "Bon",
        '5': "Nam", '6': "Sau", '7': "Bay", '8': "Tam", '9': "Chin"
    }

    num = input("Nhap so: ")
    output = " ".join(num_to_words[digit] for digit in num if digit in num_to_words)
    print("Ket qua:", output)
# Bai 7: 
def tim_bcnn():
    a = int(input("Nhap so nguyen thu nhat: "))
    b = int(input("Nhap so nguyen thu hai: "))

    def bcnn(x, y):
        return abs(x * y) // math.gcd(x, y)

    print("BCNN cua", a, "va", b, "la:", bcnn(a, b))

# Bai 8:
def ma_ascii():
    char = input("Nhap mot ky tu: ")
    print("Ma ASCII cua", char, "la:", ord(char))

# Bai 9: 
def tong_chu_so():
    num = input("Nhap mot so nguyen: ")
    total = sum(int(digit) for digit in num)
    print("Tong cac chu so la:", total)

# Bai 10:
def doi_nhi_phan():
    num = int(input("Nhap so thap phan: "))
    binary = bin(num)[2:]  
    print("So nhi phan tuong ung la:", binary)

def hien_thi_menu():
    print("Menu do uong:")
    print("1. Cafe")
    print("2. Cam vat")
    print("3. Nuoc ep ca rot")
    print("4. Nuoc loc")
    print("5. Nuoc dua")

def goi_do_uong():
    hien_thi_menu()
    lua_chon = int(input("Nhap so tuong ung voi do uong ban muon goi: "))

    menu = {
        1: "Cafe",
        2: "Cam vat",
        3: "Nuoc ep ca rot",
        4: "Nuoc loc",
        5: "Nuoc dua"
    }

    if lua_chon in menu:
        print(f"Ban da goi: {menu[lua_chon]}")
    else:
        print("Lua chon khong hop le. Vui long chon lai!")

goi_do_uong()