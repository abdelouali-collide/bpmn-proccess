from PIL import Image
import os

INPUT_DIR = "bmpn_files"
OUTPUT_DIR = "generated_images"

# Zorg dat de output folder bestaat
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Doorloop alle .bmpn bestanden
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".bmpn"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename.replace(".bmpn", ".png"))

        # Open en converteer het bestand
        try:
            img = Image.open(input_path)
            img.save(output_path)
            print(f"Generated: {output_path}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")
