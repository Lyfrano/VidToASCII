import sys
import os
import time

def main():

    fps = 30
    # allow filename as first arg, optional fps as second arg
    if sys.argv[1:]:
        filename = sys.argv[1]
    else:
        filename = input("Enter the filename to read: ")

    if len(sys.argv) > 2:
        try:
            fps = float(sys.argv[2])
        except Exception:
            pass

    # Read whole file, normalize newlines and split frames on the separator '\n?\n'
    with open(filename, "r", encoding="utf-8", errors="replace") as f:
        data = f.read()

    # Normalize CRLF and lone CR to LF for consistent splitting
    #data = data.replace('\r\n', '\n').replace('\r', '\n')

    # Split frames on the exact separator: newline, question mark, newline
    raw_frames = data.split('?')

    frames = raw_frames
    # Remove any empty frames that might result from leading/trailing separators
    #frames = [frm for frm in raw_frames if frm != '']

    # Playback loop: clear terminal between frames and print the frame (preserve its newlines)
    clear_cmd = 'cls' if os.name == 'nt' else 'clear'

    for frame in frames:
        os.system(clear_cmd)
        print(frame, end='')
        time.sleep(1.0/fps)



if __name__ == "__main__":
    main()