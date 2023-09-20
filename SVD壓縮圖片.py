from matplotlib.pyplot import imshow   # 要秀圖用的
from skimage import io  # 從網路連結讀檔
import numpy  #要計算矩陣用的

img = io.imread('https://avatars.githubusercontent.com/u/141706485?s=400&u=0c4f5e3c9240cc0b4a4b0296547f9166825c6214&v=4')
w,h=img.shape[0],img.shape[1]   # 讀出圖片的寬跟高
img_b=img[:,:,2]         #把藍色部份取出，成為 h乘w 的矩陣
img_g=img[:,:,1]         #把綠色部份取出，成為 h乘w 的矩陣
img_r=img[:,:,0]         #把紅色部份取出，成為 h乘w 的矩陣

def svd(img,d): 
    U,S,V=numpy.linalg.svd(img)
    return U[:,:d]@numpy.diag(S[:d])@V[:d,:]
#做好 Low rank approximation, c.f.  https://en.wikipedia.org/wiki/Low-rank_approximation

d=80
x= numpy.zeros((w,h,3))
x[:,:,2]=svd(img_b,d)/255   
x[:,:,1]=svd(img_g,d)/255
x[:,:,0]=svd(img_r,d)/255  # Clipping input data to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers).
imshow(x)
