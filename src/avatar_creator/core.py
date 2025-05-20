import os
from PIL import Image
import colorsys

def recolor_to_rgb(
    img: Image.Image,
    target_rgb: tuple[int, int, int]
) -> Image.Image:
    """
    Recolor an RGBA image by applying the hue & saturation of `target_rgb`,
    while preserving the original image’s brightness (value channel).
    """
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Split RGBA and get only V from HSV
    r, g, b, a = img.split()
    _, _, v = Image.merge("RGB", (r, g, b)).convert("HSV").split()

    # Compute target hue & sat in 0–255 scale
    rf, gf, bf = (c / 255.0 for c in target_rgb)
    h_t, s_t, _ = colorsys.rgb_to_hsv(rf, gf, bf)
    h_val = int(h_t * 255)
    s_val = int(s_t * 255)

    # Build new HSV and reattach alpha
    h_chan = Image.new("L", img.size, color=h_val)
    s_chan = Image.new("L", img.size, color=s_val)
    hsv = Image.merge("HSV", (h_chan, s_chan, v))
    rgb = hsv.convert("RGB")
    return Image.merge("RGBA", (*rgb.split(), a))


def load_rgba_image(dir_path: str, filename: str) -> Image.Image:
    """
    Load an image from `dir_path/filename` and convert it to RGBA.
    """
    path = os.path.join(dir_path, filename)
    return Image.open(path).convert("RGBA")

def merge_images(
    base_img: Image.Image,
    *images: Image.Image
) -> Image.Image:
    """
    Merge multiple RGBA images using alpha compositing.
    All images must be the same size.
    """
    if not images:
        raise ValueError("At least one image must be provided.")
    for img in images:
        if img.size != base_img.size:
            raise ValueError("All images must be the same size.")
        base_img = Image.alpha_composite(base_img, img)
    return base_img