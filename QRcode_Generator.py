import qrcode
import random
import string
import json
from datetime import datetime

def random_string(length=6):
    """Generate random uppercase string"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_random_qr():
    # Create random product details
    product = {
        "item_name": "Item_" + random_string(4),
        "description": "Random product description",
        "product_code": random_string(8),
        "type": random.choice(["Capsule", "Tablet", "Bottle", "Box"]),
        "size": str(random.choice([10, 20, 50, 100])) + " mg",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Convert to JSON string
    data = json.dumps(product)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Save as PNG
    img = qr.make_image(fill="black", back_color="white")
    filename = f"qr_{product['product_code']}.png"
    img.save(filename)

    print(f"✅ QR code saved as {filename}")
    print("QR Content:", product)

if __name__ == "__main__":
    generate_random_qr()
