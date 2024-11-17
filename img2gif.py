'''
# Animated GIF Creator from Image Folder
This script allows you to create an animated GIF from a set of images stored in a specified folder. 
The images are processed in alphabetical order, resized to uniform dimensions, and then combined into a GIF with a customizable frame duration.

Awesome for when you want to add into your README.md a secqience of screenshots for example.

November 16, 2024
Notes:
I wrote this since using the ususal tools, the duration of the transition was overriten, and the gifs were anumated too quickly.
Key Changes:
- Pillow for GIF Creation: Instead of using imageio for GIF creation, I now use Pillow which gives me direct control over the duration attribute.
- Duration Conversion: The duration parameter in Pillow's save method expects milliseconds, so I multiply frame_duration by 1000 (frame_duration * 100 for simplicity, assuming it's close enough for my needs).
- Loop Setting: loop=0 means the GIF will loop indefinitely.
- Image Conversion: Images are converted to palette mode ('P') for better GIF compatibility and possibly better handling of frame timing.

## Author Information
- **Author**: Nic Cravino
- **Email**: spidernic@me.com 
- **LinkedIn**: [Nic Cravino](https://www.linkedin.com/in/nic-cravino)
- **Date**: November 16, 2024


## License: Apache License 2.0 (Open Source)
This tool is licensed under the Apache License, Version 2.0. This is a permissive license that allows you to use, distribute, and modify the software, subject to certain conditions:

- **Freedom of Use**: Users are free to use the software for personal, academic, or commercial purposes.
- **Modification and Distribution**: You may modify and distribute the software, provided that you include a copy of the Apache 2.0 license and state any significant changes made.
- **Attribution**: Original authorship and contributions must be acknowledged when redistributing the software or modified versions of it.
- **Patent Grant**: Users are granted a license to any patents covering the software, ensuring protection from patent claims on original contributions.
- **Liability Disclaimer**: The software is provided "as is," without warranties or conditions of any kind. The authors and contributors are not liable for any damages arising from its use.

For full details, see the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
'''

import os
from PIL import Image
import imageio  # For image conversion
import numpy as np

def create_gif_from_images_pillow(folder_path, output_gif_path, frame_duration=30.0):
    # List to store the processed images
    images = []
    
    # Get all image files from the folder sorted alphabetically
    image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])
    if not image_files:
        print("No image files found in the specified folder.")
        return

    # Find the dimensions of the first image to standardize size
    base_width, base_height = Image.open(os.path.join(folder_path, image_files[0])).size

    # Process each image in alphabetical order
    for img_file in image_files:
        img_path = os.path.join(folder_path, img_file)
        
        # Open the image
        with Image.open(img_path) as img:
            # Resize image to match the base dimensions while keeping aspect ratio
            img = img.resize((base_width, base_height), Image.LANCZOS)
            images.append(img.convert('P'))  # Convert to palette mode for GIF compatibility

    # Save all images as a GIF, specifying the inter-frame delay
    images[0].save(output_gif_path, save_all=True, append_images=images[1:], optimize=False, duration=frame_duration * 100, loop=0)

# Example usage
folder_path = './'  # Replace with your actual folder path
output_gif_path = 'screen.gif'  # Name for your output GIF file

create_gif_from_images_pillow(folder_path, output_gif_path, frame_duration=10.0)