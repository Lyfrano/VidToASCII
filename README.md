<center> 
   <h1> A python based app that converts videos to ASCII art </h1> 
</center>

<p align="center">
      
   <img src="https://github.com/user-attachments/assets/54f2f96e-8f24-40d4-bc88-67b35a1d1e39" width="500" height="500"/>
      
</p>

# videoInCMD

Convert videos into ASCII art and play them directly in your terminal

## Requirements

Video Converter :

- Python 3.x
- `ffmpeg` (included in `ffmpeg-2025\bin\` folder)
- scikit-image
- numpy

Video Player :

- Python 3.x

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install scikit-image numpy

- The renderer does not have any requirements other than python and can be used to play any videos converted by the converter

## Usage

Run the script with optional video file argument:

```bash
python videoInCMD.py [video_file.mp4]
```

Or simply run without arguments:
```bash
python videoInCMD.py
```

To display a saved video simply do :
```bash
python renderer.py (optional)[videoname] (optional)[fps]
```




 

