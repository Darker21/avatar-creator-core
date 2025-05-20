# Avatar Creator Core

[![Build and Test Python Package](https://github.com/Darker21/avatar-creator-core/actions/workflows/build-and-test.yml/badge.svg?branch=develop)](https://github.com/Darker21/avatar-creator-core/actions/workflows/build-and-test.yml)

A Python library for recoloring white-hair assets and compositing avatar images using Pillow.

## Features

- Recolor hair images to any RGB color while preserving shading.
- Composite hair and face images to create custom avatars.
- Simple API for loading, recoloring, and merging images.

## Installation

```sh
pip install pillow
```

Or install from source:

```sh
pip install .
```

## Usage

Example script ([dev/main.py](dev/main.py)):

```python
import src.avatar_creator.core as core

# Load images
face_img = core.load_rgba_image("content/face", "face_1.png")
hair_img = core.load_rgba_image("content/hair", "mid-length.png")

# Recolor hair to orange
hair_img = core.recolor_to_rgb(hair_img, (255, 144, 25))

# Composite hair over face
avatar = core.merge_images(face_img, hair_img)

# Save result
avatar.save("output.png")
```

## API

### [`avatar_creator.core.recolor_to_rgb`](src/avatar_creator/core.py)

```python
recolor_to_rgb(img: Image.Image, target_rgb: tuple[int, int, int]) -> Image.Image
```
Recolors an RGBA image to the target RGB color, preserving the original brightness.

### [`avatar_creator.core.load_rgba_image`](src/avatar_creator/core.py)

```python
load_rgba_image(dir_path: str, filename: str) -> Image.Image
```
Loads an image from a directory and converts it to RGBA.

### [`avatar_creator.core.merge_images`](src/avatar_creator/core.py)

```python
merge_images(base_img: Image.Image, *images: Image.Image) -> Image.Image
```
Alpha-composites multiple RGBA images. All images must be the same size.

## License

MIT License. See [LICENSE](LICENSE).