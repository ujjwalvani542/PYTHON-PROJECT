import qrcode
url=input("ENTER YOUR URL").strip()
File_Path="C:\\Users\\dell\\OneDrive\\Desktop\\QE.PNG"

qr=qrcode_QRcode()
qr_add_data(url)

img=qr.make_image()
img.save(File_Path)
