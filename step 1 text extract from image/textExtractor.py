from PIL import Image
from pytesseract import pytesseract


try:
    for i in range(1, 100):
  # Defining paths to tesseract.exe
  # and the image we would be using

  # set the path of tesseract
      path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
      image_path = "da"+ str(i)+".jpeg"
  
  # Opening the image & storing it in an image object
      img = Image.open(image_path)
    
  # Providing the tesseract executable
  # location to pytesseract library
      pytesseract.tesseract_cmd = path_to_tesseract
  
  # Passing the image object to image_to_string() function
  # This function will extract the text from the image
      text = pytesseract.image_to_string(img)
    
  # Displaying the extracted text
    #   print(text[:-1])

      file = open("extraction" + str(i) + ".txt", "w") 
      file.write(text[:-1]) 
      text = ""
      file.close() 
except Exception as e:
  print("An exception occurred: ", e) 
