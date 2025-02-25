import os
import cv2
import mimetypes
import numpy as np
from PIL import Image

def verify_files(directory="."):
    errors = []
    print(f"Checking files in: {os.path.abspath(directory)}\n")

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type, _ = mimetypes.guess_type(file_path)

            try:
                # Check if the file is an image
                if file_type and file_type.startswith("image"):
                    # Try opening with OpenCV
                    img = cv2.imread(file_path)
                    if img is None:
                        raise ValueError("Corrupt or unreadable image (OpenCV)")
                    
                    # Try opening with PIL
                    with Image.open(file_path) as img_pil:
                        img_pil.verify()  # Check for corruption
                    
                    print(f"✅ Image loaded successfully: {file_path}")

                else:
                    # Attempt to read the file as a text/binary file
                    with open(file_path, "rb") as f:
                        f.read()
                    print(f"✅ File loaded successfully: {file_path}")

            except Exception as e:
                errors.append((file_path, str(e)))
                print(f"❌ Error loading {file_path}: {e}")

    if errors:
        print("\nSome files failed to load:")
        for path, error in errors:
            print(f"- {path}: {error}")
    else:
        print("\nAll files loaded successfully!")

# Run the verification
verify_files()
