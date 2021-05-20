def kiemtra(a,b,c):
    if a in tinhthanh_covid:
        print("Tỉnh", a, "có", Counter(tinhthanh_covid)[a], "người bị nhiễm Covid")
    else:
        print("Tỉnh", a, "chưa ghi nhận có người nhiễm Covid")
    if b in quanhuyen_covid:
        print("Quận/Huyện", b, "có", Counter(quanhuyen_covid)[b], "người bị nhiễm covid")
    else:
        print("Quận/Huyện", b, "chưa ghi nhận có người nhiễm Covid")
    if c in quanhuyen_covid:
        print("Phường/Xã", c, "có", Counter(phuongxa_covid)[c], "người bị nhiễm covid")
    else:
        print("Phường/Xã", c, "chưa ghi nhận có người nhiễm Covid")  
class nguoidan:
    def __init__(self,hoten,namsinh,cmnd,tinhthanh,quanhuyen,phuongxa,sdt):
        self.hoten = hoten
        self.namsinh = namsinh
        self.cmnd = cmnd
        self.sdt = sdt
        self.tinhthanh = tinhthanh
        self.quanhuyen = quanhuyen
        self.phuongxa = phuongxa
    def show(self):
        print("Họ và tên: ",self.hoten)
        print("Năm sinh: ",self.namsinh)
        print("CMND/CCCD/Hộ chiếu: ",self.cmnd)
        print("Số điện thoại: ",self.sdt)
        print("Tỉnh thành: ",self.tinhthanh)
        print("Quận/Huyện: ",self.quanhuyen)
        print("Phường/Xã: ",self.phuongxa)
    def khaibao():
        a = nguoidan(0,0,0,0,0,0,0)
        a.hoten = input('Họ và tên: ')
        a.namsinh = input("Năm sinh: ")
        a.cmnd = input("CMND/CCCD/Hộ chiếu: ")
        a.sdt = input("Số điện thoại: ")
        a.tinhthanh = input("Tỉnh thành: ")
        a.quanhuyen = input("Quận/Huyện: ")
        a.phuongxa = input("Phường/Xã: ")
        return a
class benhnhan(nguoidan):
    pass
#     def add_benhnhan():
#         super().khaibao()
#     def __init__(self,hoten,namsinh,cmnd,tinhthanh,quanhuyen,phuongxa,sdt):
#         super().__init__(hoten,namsinh,cmnd,tinhthanh,quanhuyen,phuongxa,sdt)
    
DS_Nguoidan = []
DS_Benhnhan = []

import datetime

while True:
    print(''' ========================================
        1. Khai báo y tế
        2. Nhập bệnh nhân Covid (Admin)
        3. Kiểm tra số ca nhiễm Covid ở nơi bạn
        4. Xem tình hình Covid
        0. Thoat
  ========================================
        ''')
    chon = int(input('Moi ban chon chuc nang : '))
    print('****************************************')
    if chon == 1 :
        a = 0
        Nguoidan_khaibao = nguoidan.khaibao()
        DS_Nguoidan.append(Nguoidan_khaibao)
    elif chon == 2 :
        password = input('Nhap mat khau: ')
        if password == 'admin':
            benhnhan_add = benhnhan.khaibao()
            DS_Benhnhan.append(benhnhan_add)
        else : print('Mat khau sai')
    elif chon == 3 :
        phuong_xa = input('Phuong/Xa:')
        quan_huyen = input('Quan/huyen:')
        tinhthanh = input('Tinh thanh: ')
        check(phuong_xa,quan_huyen,tinhthanh)
#     elif chon == 4:
#         print('Việt Nam tính đến ngày', datetime.datetime.now(), 'ghi nhận có', len(DS_Benhnhan))
#         print("'Trong đó có:
#               '")     
    else :
        break

