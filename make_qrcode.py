import qrcode #library to make qr codes
import requests #library to make HTTP requests
from io import BytesIO #used to create binary stream to hold image data

def generate_qr_code(url, output_filename):
    qr = qrcode.QRCode( #create qr code object and specify parameters
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url) #give qr code object the url
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")#generate qr code image
    img.save(output_filename)#save it

def main():
    url = input("Enter the URL: ") #take user's URL input
    qr_filename = input("Enter the output QR code filename (e.g., qr_code.png): ")#name the image file what the user inputs

    try:
        response = requests.get(url) #make get request on user's url
        response.raise_for_status()  # Check for valid response

        generate_qr_code(url, qr_filename)# if that url works then run qr code function
        print(f"QR code generated and saved as {qr_filename}")#tell user image is generated
    except requests.exceptions.RequestException as e:#if the get request doesn't work then print error
        print("Error:", e)

if __name__ == "__main__":
    main()
