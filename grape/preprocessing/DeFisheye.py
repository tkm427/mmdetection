from defisheye import Defisheye
import matplotlib.pyplot as plt

dtype = 'stereographic'
format = 'fullframe'
fov = 180
pfov = 120
img = "./hoge.png"
img_out = f"./out/test_{dtype}_{fov}_to_{pfov}.png"

obj = Defisheye(img, dtype=dtype, format=format, fov=fov, pfov=pfov)

# To save image locally 
obj.convert(outfile=img_out)