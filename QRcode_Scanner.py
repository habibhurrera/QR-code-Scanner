import cv2
import csv
from datetime import datetime
from pyzbar.pyzbar import decode

# CSV file name
file_name = "qr_data.csv"

# Create CSV if not exists (with only timestamp column first)
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Field1", "Field2", "Field3", "Field4", "Timestamp"])  # Generic headers

# Open webcam
cap = cv2.VideoCapture(0)

# To avoid duplicate continuous detections
scanned_data = set()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # ✅ Mirror the camera (horizontal flip)
    frame = cv2.flip(frame, 1)

    # Decode QR codes
    qr_codes = decode(frame)

    for qr in qr_codes:
        data = qr.data.decode("utf-8")

        if data not in scanned_data:
            scanned_data.add(data)

            # Split QR data into fields (comma separated)
            fields = data.split(",")

            # Add timestamp as last field
            fields.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            # Save to CSV
            with open(file_name, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(fields)

            print(f"QR Saved: {fields}")

        # Draw rectangle around QR
        (x, y, w, h) = qr.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)

    # Show mirrored camera feed
    cv2.imshow("QR Code Scanner (Mirrored)", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
