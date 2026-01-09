import qrcode

website_link ='https://kishu01karb.github.io/Animate-Images-with-keyframes-using-CSS/'
#'https://youtu.be/_yRJsecDjjc?si=zl1WFGYUt_of1bUz'

qr = qrcode.QRCode(version=1, box_size= 5 ,border= 5)

qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color ='black', back_color ='white')

img.save('QR_Code.png')
