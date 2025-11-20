import os
import sys
import time
import asyncio
import skimage as ski
from skimage.transform import resize

ffmpeg_path = r"ffmpeg-2025\bin\ffmpeg.exe"
vid_name = "input_video.mp4"
out_name = r"temp\output_video"
vid_fps = 30

zSIZE = [" ",".","o","O","@"]

dimensions = (50, 150)




def main():
    global vid_name


    if sys.argv[1:]:
        vid_name = sys.argv[1]


    videoToFrames()

    processed_frame_file = []
    os.system('cls' if os.name == 'nt' else 'clear')

    frame_files = sorted([f for f in os.listdir(r'.\temp') if f.startswith('output_video') and f.endswith('.png')])

    time_at_start = time.time()

    for frame_file in frame_files:
        frame = ski.io.imread(os.path.join(r'.\temp', frame_file))
        processed_frame_file.append(processFrame(frame))

        print(f"Processed frame: {frame_file} Out of: {len(frame_files)}")

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Video Ready to Play. Press ENTER to start.  In :{time.time() - time_at_start}")
    input()


    time_at_frame1 = time.time()

    for frame in processed_frame_file:
        time_elapsed = time.time()
        os.system('cls' if os.name == 'nt' else 'clear')
        drawCanvas(frame)

        wait_time = (1/vid_fps) - (time.time() - time_elapsed)
        if wait_time > 0:
            time.sleep(wait_time)

    time_elapsed = time.time() - time_at_frame1   
    print(f"Video played in {time_elapsed} seconds.")



def pixelToStr(pixel):
    if pixel < 0.2:
        return zSIZE[0]
    elif pixel < 0.4:
        return zSIZE[1]
    elif pixel < 0.6:   
        return zSIZE[2]
    elif pixel < 0.8:
        return zSIZE[3]
    else:
        return zSIZE[4]
    

def videoToFrames():
    #empty temp folder
    temp_folder = r'.\temp'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    else:
        for f in os.listdir(temp_folder):
            os.remove(os.path.join(temp_folder, f))


    os.system( ffmpeg_path + ' -i '  + vid_name + ' -vf fps=' + str(vid_fps) + ' ' + out_name + '%04d.png')


def drawCanvas(frame):

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            pixel = frame[i-1][j-1]
            pixel_str = pixelToStr(pixel)
            print(pixel_str, end='')
        print('')


def asyncFrameProcessing(frame):
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, process_frame, frame)

def processFrame(frame):
    # Example processing: convert to grayscale
    gray_frame = ski.color.rgb2gray(frame)

    # Resize to target dimensions
    gray_frame = resize(gray_frame, dimensions, anti_aliasing=True)

    return gray_frame



if __name__ == "__main__":
    main()