import os
import sys
import time
import asyncio
import json
import skimage as ski
from skimage.transform import resize

ffmpeg_path = r"ffmpeg-2025\bin\ffmpeg.exe"
vid_name = "input_video.mp4"
out_name = r"temp\output_video"
vid_fps = 30
fps_control = False


frameSTR = ""

zSIZE = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

dimensions = (45, 80)

def initialize():
    global vid_name, vid_fps, dimensions, fps_control, displayInRealTime

    print('Current video file:', vid_name)
    input_vid = input('Enter video file name (or press ENTER to keep current): ')
    if input_vid.strip():
        vid_name = input_vid.strip()


    input_fps = input(f'Enter video FPS (current: {vid_fps}): ')
    if input_fps.strip():
        vid_fps = int(input_fps.strip())


    print("Your window dimensions are currently : ")
    os.system("mode con /status")
    input_dim = input(f'Enter dimensions as - height,width - (current: {dimensions[0]},{dimensions[1]}): ')
    if input_dim.strip():
        height, width = map(int, input_dim.strip().split(','))
        dimensions = (height, width)


    print("")
    


def main():
    global vid_name, vid_fps, dimensions, frameSTR, fps_control

    displayInRealTime = False


    if sys.argv[1:]:
        vid_name = sys.argv[1]

    initialize()

    displayInRealTime = input(f'Display video in real-time? (current: {"Yes" if displayInRealTime else "No"}) [y/n]: ').strip().lower() == 'y'

    if displayInRealTime == True:
        input_fps_control = input(f'Enable FPS control? (current: {"Yes" if fps_control else "No"}) [y/n]: ')
        if input_fps_control.strip().lower() == 'y':
            fps_control = True
        else:
            fps_control = False

    print("")


    videoToFrames()

    processed_frame_file = []
    os.system('cls' if os.name == 'nt' else 'clear')
    

    frame_files = sorted([f for f in os.listdir(r'.\temp') if f.startswith('output_video') and f.endswith('.jpeg')])

    time_at_start = time.time()

    for frame_file in frame_files:
        frame = ski.io.imread(os.path.join(r'.\temp', frame_file))

        processed_frame_file.append(processFrame(frame))

        print(f"Processed frame: {frame_file} Out of: {len(frame_files)}")

    os.system('cls' if os.name == 'nt' else 'clear')

    if displayInRealTime:
        print(f"Video Ready to Play. Press ENTER to start.   # Done in :{time.time() - time_at_start}")
    else:
        print(f"Video Ready to Save. Press ENTER to continue.   # Done in :{time.time() - time_at_start}")

    input()

    time_at_frame1 = time.time()

    if displayInRealTime:
        if fps_control:
            for frame in processed_frame_file:
                time_elapsed = time.time()
                drawCanvas(frame)
                wait_time = (1/vid_fps) - (time.time() - time_elapsed)
                if wait_time > 0:
                    time.sleep(wait_time)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(frameSTR)

                
        else:
            for frame in processed_frame_file:
                time_elapsed = time.time()
                drawCanvas(frame)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(frameSTR)
    else:
        saveVideoFramesAsText( processed_frame_file,r'.\output\output_' + vid_name + '.txt' )


    time_elapsed = time.time() - time_at_frame1   
    

    print(f"Video played/saved in {time_elapsed} seconds.")
    



def pixelToStr(pixel):
    if pixel < 0.1:
        return zSIZE[0]
    elif pixel < 0.2:
        return zSIZE[1]
    elif pixel < 0.3:   
        return zSIZE[2]
    elif pixel < 0.4:
        return zSIZE[3]
    elif pixel < 0.5:
        return zSIZE[4]
    elif pixel < 0.6:
        return zSIZE[5]
    elif pixel < 0.7:
        return zSIZE[6]
    elif pixel < 0.8:
        return zSIZE[7]
    elif pixel < 0.9:
        return zSIZE[8]
    else :
        return zSIZE[9]


def videoToFrames():
    #empty temp folder
    temp_folder = r'.\temp'
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    else:
        for f in os.listdir(temp_folder):
            os.remove(os.path.join(temp_folder, f))


    os.system(
    ffmpeg_path
    + ' -i ' + vid_name
    + ' -vf "fps=' + str(vid_fps) + ',scale=-1:' + str(max(dimensions)) + '" '
    + out_name + '%04d.jpeg' )



def drawCanvas(frame):

    global frameSTR
    frameSTR = ""

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            
            pixel = frame[i-1][j-1]
            pixel_str = pixelToStr(pixel)
            frameSTR += pixel_str
        frameSTR += '\n'

def saveVideoFramesAsText(frames, out_file):

    print(f"Saving video frames to {out_file}...")

    with open(out_file, 'w') as f:

        f.write(str(vid_fps)+"\n")

        for frame in frames:
            for i in range(dimensions[0]):
                for j in range(dimensions[1]):

                    pixel = frame[i-1][j-1]
                    pixel_str = pixelToStr(pixel)

                    f.write(pixel_str)

                f.write('\n')

            f.write('\n?\n')  # Separate frames by newline and ?



    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Video frames saved to {out_file}.")


def asyncFrameProcessing(frame):
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, processFrame, frame)

def processFrame(frame):


    gray_frame = resize(frame, dimensions, anti_aliasing=True)

    gray_frame = ski.color.rgb2gray(gray_frame)

    

    return gray_frame



if __name__ == "__main__":
    main()