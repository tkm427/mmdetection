import sys
import os 
import numpy as np
import vrProjector
import cv2
from mpmath import mp

#画像の読み込み.入力画像が左側か右側か知っておく必要あり．

def rotate_fisheye(input_img, output_img, rotate):
    side = 'right'

    if( (side != 'right') and (side !='left') ):
        print( '3rd argument must be "right" or "left"' ) 
        sys.exit()

    fisheye_raw = cv2.imread( input_img, cv2.IMREAD_COLOR )
    blanc_img = np.zeros( (fisheye_raw.shape[0], fisheye_raw.shape[1], 3 ), np.uint8 )
    dualfisheye = cv2.hconcat( [blanc_img, fisheye_raw ] )
    
    #一時保存
    cv2.imwrite( 'dualfish_fix.png', dualfisheye )

    #キューブマップにしてみる
    source = vrProjector.SideBySideFisheyeProjection()
    source.loadImage('dualfish_fix.png')

    # rotate: 左に回転
    source.reprojectToThis(source, rotate= rotate)
    source.saveImage_half(output_img, side)

def fisheye_to_cubemap_folder(input_folder, output_folder):
    for image_path in os.listdir(input_folder):
        rotate_fisheye(input_folder + image_path, output_folder + image_path)

def rotate_fisheye_folder(input_folder, output_folder, rotate):
    for image_path in os.listdir(input_folder):
        rotate_fisheye(input_folder + image_path, output_folder + image_path, rotate)
        # 画像を90度回転
        img = cv2.imread(output_folder + image_path)
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(output_folder + image_path, img)
        rotate_fisheye(output_folder + image_path, output_folder + image_path, rotate)
        # 画像を-90度回転
        img = cv2.imread(output_folder + image_path)
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(output_folder + image_path, img)

input_folder = '/Users/nobu/research/mmdetection-grape/fisheye_to_cubemap/input/'
output_folder = '/Users/nobu/research/mmdetection-grape/fisheye_to_cubemap/output/'
rotate_fisheye_folder(input_folder, output_folder, mp.pi/6)