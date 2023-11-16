import qrcode

def generate_qr_code(data, file_name):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_name)

if __name__ == "__main__":
    # Example usage
    data_to_encode ="add you info here..."
    output_file = "example_qr_code.png"

    generate_qr_code(data_to_encode, output_file)
    print(f"QR code generated and saved as {output_file}")
