import qrcode
from PIL import Image
import base64
from datetime import datetime

def generate_qr():

    print("this process for create qr code")

    data = "https://ecpe.nu.ac.th"
    qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    #image=qr.make_image(fill_color="black", back_color="white")
    image=qr.make_image(fill_color="black", back_color="GreenYellow")



    now = datetime.now()  # current date and time
    date_time = now.strftime("%m%d%Y_%H%M%S")
    fileName = "qrcode_"+date_time+".png"

    image.save("./public/images/"+fileName)  # Save the image to a file

    #read the saved image with built-in PIL library
    #image = Image.open("./public/images/"+fileName)
    ##convert the images  to hex rawdata
    #raw_data = image.tobytes()
    #print(raw_data)  # This will print the raw data of the image

    # image_data = base64.b64encode(raw_data).decode('utf-8')
    # print(image_data)
    # return image_data

    # base64_bytes = base64.b64encode(raw_data)
    # base64_string = base64_bytes.decode("utf-8")
    # return base64_string

    with open("./public/images/"+fileName, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return image_data


def generate_qr_v2(options):
    """ Generate a QR code with the given options.
    Args:
        options (dict): A dictionary containing the options for the QR code.
            It should contain 'data', 'version', 'error_correction', 'box_size', and 'border'.
    Returns:
        str: The base64 encoded string of the generated QR code image.  
    """

    print("this process for create qr code by passing data")

    #print(type(options['version']))

    qr = qrcode.QRCode(version=int(options['version']),
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=int(options['box_size']),
                    border=int(options['border']) if 'border' in options else 4)
    
    qr.add_data(options['data'])
    qr.make(fit=True)

    image=qr.make_image(fill_color=options['fill_color'], back_color=options['back_color'])

    now = datetime.now()  # current date and time
    date_time = now.strftime("%m%d%Y_%H%M%S")
    fileName = "qrcode_"+date_time+".png"

    image.save("./public/images/"+fileName)  # Save the image to a file

    with open("./public/images/"+fileName, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return image_data
