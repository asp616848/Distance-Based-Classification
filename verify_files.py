import os
import cv2
import mimetypes
from PIL import Image

def verify_files(directory="."):
    files_to_check = {
        "wandb-workspace.png",
        "wandb-project_view.png",
        "Plaksha_Faculty.jpg",
        "Dr_Shashi_Tharoor.jpg"
    }
    
    errors = []
    print(f"Checking specified files in: {os.path.abspath(directory)}\n")
    
    for file in files_to_check:
        file_path = os.path.join(directory, file)
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            errors.append((file_path, "File not found"))
            continue
        
        file_type, _ = mimetypes.guess_type(file_path)
        
        try:
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
                print(f"⚠️ Not an image file: {file_path}")
        
        except Exception as e:
            errors.append((file_path, str(e)))
            print(f"❌ Error loading {file_path}: {e}")
    
    if errors:
        print("\nSome files failed to load:")
        for path, error in errors:
            print(f"- {path}: {error}")
    else:
        print("\nAll specified files loaded successfully!")

# Run the verification
verify_files()
