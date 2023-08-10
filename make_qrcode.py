import qrcode
import requests
from io import BytesIO

def generate_qr_code(url, output_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)

def main():
    url = input("Enter the URL: ")
    qr_filename = input("Enter the output QR code filename (e.g., qr_code.png): ")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for valid response

        generate_qr_code(url, qr_filename)
        print(f"QR code generated and saved as {qr_filename}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
