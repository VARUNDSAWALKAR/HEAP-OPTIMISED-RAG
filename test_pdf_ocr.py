from pdf2image import convert_from_path
import pytesseract

pdf_path = r"C:\Users\nidag\Downloads\unit 1 (4).pdf"

print("Converting PDF to images...")
images = convert_from_path(pdf_path)

print("Total pages:", len(images))

text = ""
for img in images:
    text += pytesseract.image_to_string(img)

print("\nOCR TEXT SAMPLE:\n")
print(text[:1000])
