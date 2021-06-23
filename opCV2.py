import cv2

def resizeFunction(photo,width, height, name):
    image = cv2.imread(photo)
    # name = "Resized photos/" + saveName + ".jpg"
    dim = (width, height)
    interpolation = cv2.INTER_AREA
    resized = cv2.resize(image, dim, interpolation)
    cv2.imwrite(name,resized)