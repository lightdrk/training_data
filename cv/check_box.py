import subprocess
import cv2

try:
    subprocess.check_call(['pip','install','opencv2'])
    print("success")
except subprocess.CalledProcessError:
    print("unsucess")

imagePath = r'C:\Users\arch\Desktop\boxfile\test1.jpeg'
image = cv2.imread(imagePath)
cv2.rectangle(image,(234,202),(234+177,202+19),(0, 255, 0), 2)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()