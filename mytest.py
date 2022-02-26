from tifffile import TiffFile
import cv2

with TiffFile('./test.tif') as tif:
    for page in tif.pages:
        image = page.asarray()
        cv2.imshow('image',image)

        cv2.waitKey(0) 
        cv2.destroyAllWindows()
        break