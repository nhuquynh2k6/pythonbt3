from datetime import date
ho_ten=input("Nhap ho va ten: ")
ngay_sinh_str=input("Nhap ngay sinh (dd/mm/yyyy): ")
ngay_hien_tai=date.today()
ngay_sinh_parts=ngay_sinh_str.split('/')
ngay=int(ngay_sinh_parts[0])
thang=int(ngay_sinh_parts[1])
nam=int(ngay_sinh_parts[2])
tuoi=ngay_hien_tai.year-nam
ngay_sinh_hop_le=False
try:
    ngay_sinh=date(nam,thang,ngay)
    if ngay_sinh<=ngay_hien_tai:
        ngay_sinh_hop_le=True
except ValueError:
    pass
if ngay_sinh_hop_le:
    if tuoi==0:
        tuoi=1
    print(f"Ho va ten: {ho_ten}")
    print(f"Tuoi: {tuoi}")
else:
    print("Ngay sinh khong hop le")