# Animated GIF Creator from Image Folder
## Author Information
- **Author**: Nic Cravino
- **Email**: spidernic@me.com 
- **LinkedIn**: [Nic Cravino](https://www.linkedin.com/in/nic-cravino)
- **Date**: NOvember 16, 2024

This script allows you to create an animated GIF from a set of images stored in a specified folder. The images are processed in alphabetical order, resized to uniform dimensions, and then combined into a GIF with a customizable frame duration.

## Features

- **Automatic Processing**: Loads all compatible image files from a directory.
- **Uniform Resizing**: Resizes images to match the dimensions of the first image in the folder.
- **Custom Frame Duration**: You can set the duration for which each frame is displayed in the GIF.
- **GIF Loop**: The GIF is set to loop indefinitely.

## Requirements

- Python 3.x
- Pillow (PIL Fork)
- Numpy

You can install the required packages using pip:

```bash
pip install Pillow numpy
```

## Usage

1. **Setup**: Place your images in a folder. Ensure images are named in a way that sorting alphabetically will give you the correct sequence (e.g., `image001.jpg`, `image002.jpg`, etc.).

2. **Script Execution**:

   ```bash
   python animated_gif_creator.py
   ```

   Before running, make sure to edit the `folder_path` and `output_gif_path` variables in the script to match your setup.

```python
folder_path = 'path/to/your/folder'  # Path to the directory containing images
output_gif_path = 'output.gif'       # Desired path for the output GIF
```

3. **Customize Frame Duration**:
   
   If you want to change how long each frame is displayed, adjust the `frame_duration` parameter when calling the function:

   ```python
   create_gif_from_images_pillow(folder_path, output_gif_path, frame_duration=10.0)
   ```

   Here, `frame_duration` is set to 10 seconds, but you can change this value as needed.

## Code

The main script looks like this:

```python
import os
from PIL import Image

def create_gif_from_images_pillow(folder_path, output_gif_path, frame_duration=10.0):
    # ... (Function code as provided)

# Usage example
folder_path = 'path/to/your/folder'
output_gif_path = 'output.gif'

create_gif_from_images_pillow(folder_path, output_gif_path, frame_duration=10.0)
```

## Troubleshooting

- **GIF Plays Too Fast**: If the GIF playback speed seems incorrect, try viewing it in different applications or browsers. Some viewers might not respect the delay settings properly.
- **Images Not Loading**: Make sure all images are in a format Pillow can handle (JPEG, PNG, etc.).
- **Dimension Mismatch**: If you encounter issues with image dimensions, ensure all images are in a format that can be processed by PIL for resizing.

## Contributing

Feel free to fork this project, make changes, and submit pull requests for improvements or additional features.

## License

This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). Here are the key points:

- You can use, modify, and distribute this software freely.
- Any modifications or derivative works must be licensed under the same terms.
- The software is provided "as is" without warranty of any kind.
- Trademarks are not covered by this license.

For full license details, please refer to the LICENSE file in this repository.