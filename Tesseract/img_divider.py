import cv2

def divide(img_path, 縦or横, div_num):
    img = cv2.imread(img_path)
    print(img.shape)
    h, w = img.shape[0], img.shape[1]

    imgs = []
    if 縦or横 == '縦':
        dw = int(w / div_num)
        for i in range(div_num):
            imgs.append( img[:, dw*i:dw*(i+1)] )
            pass
    elif 縦or横 == '横':
        dh = int(h / div_num)
        for i in range(div_num):
            imgs.append( img[dh*i:dh*(i+1), :] )
            pass
    
    #画像保存 imwrite(filename, image)
    im_paths = []
    count = 0
    for im in imgs:
        count += 1
        imgPath = "result/divd{0}.png".format(count)
        cv2.imwrite(imgPath, im)
        im_paths.append(imgPath)

    return im_paths


if __name__ == "__main__":
    imgs = divide('../test.png', '横', 4)

