"""
Avatar Creator

This script allows users to create a composite avatar image by selecting a face and hair style,
and recoloring the hair to a user-specified color. The script loads image assets from the
'content/face' and 'content/hair' directories, recolors the hair image, and overlays it on the
selected face image. The final avatar is saved as 'output.png' in the project directory.

Dependencies:
    - Pillow (PIL)
    - colorsys (standard library)

Directory Structure:
    content/
        face/
            [face image files]
        hair/
            [hair image files]
"""

import os
import avatar_creator.core as core

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HAIR_DIR = os.path.join(BASE_DIR, "content", "hair")
FACE_DIR = os.path.join(BASE_DIR, "content", "face")
OUTPUT_PATH = os.path.join(BASE_DIR, "output.png")

def main():
    """
    Main function to run the avatar creator workflow:
        1. Lists available hair and face image files.
        2. Prompts the user to select a hair and face option.
        3. Prompts the user for a hair color (RGB or hex).
        4. Loads and recolors the hair image.
        5. Loads the face image.
        6. Alpha-composites the hair onto the face.
        7. Saves the resulting avatar image.
    """
    # List available hair and face files
    hair_files = [
        f for f in os.listdir(HAIR_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    face_files = [
        f for f in os.listdir(FACE_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    print("Available hair options:")
    for idx, fname in enumerate(hair_files, 1):
        print(f"{idx}: {fname}")
    hair_choice = int(input("Select hair option by number: ")) - 1
    hair_file = hair_files[hair_choice]

    print("Available face options:")
    for idx, fname in enumerate(face_files, 1):
        print(f"{idx}: {fname}")
    face_choice = int(input("Select face option by number: ")) - 1
    face_file = face_files[face_choice]

    # Load and recolor hair image
    hair_img = core.load_rgba_image(os.path.join(HAIR_DIR, hair_file))

    # Ask user for hair color as R,G,B input or hex code
    hair_color_input = input("Enter hair color as R,G,B (e.g. 255,144,25) or hex (e.g. #FF9019): ").strip()
    if hair_color_input.startswith("#"):
        hex_code = hair_color_input.lstrip("#")
        if len(hex_code) == 6:
            hair_color = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
        else:
            raise ValueError("Hex color must be 6 digits (e.g. #FF9019)")
    else:
        hair_color = tuple(int(c.strip()) for c in hair_color_input.split(","))
    hair_img = core.recolor_to_rgb(hair_img, hair_color)

    # Load face image
    face_img = core.load_rgba_image(os.path.join(FACE_DIR, face_file))

    # Composite hair over face (both must be same size)
    combined = core.merge_images(face_img, hair_img)

    # Save output
    combined.save(OUTPUT_PATH)
    print(f"✅ Saved combined image to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
