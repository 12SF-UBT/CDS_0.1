import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread(r"C:\Users\udayb\OneDrive\Pictures\Saved Pictures\n1.webp")
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_RGB))
cv2.imshow("Input", image)
cv2.waitKey(0)
