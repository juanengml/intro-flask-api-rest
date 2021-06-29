from flask_opencv_streamer.streamer import Streamer
#from cvlib.object_detection import draw_bbox
from datetime import datetime as dt 
from datetime import timedelta
import cv2
#import cvlib as cv

# http://insecam.org/en/view/912189/ 

from console_logging.console import Console
console = Console()

# test 
detec = []

#(1076, 184)
port = 8080	
require_login = False
streamer = Streamer(port, require_login)
        
endpoint = "http://ec2-54-91-136-29.compute-1.amazonaws.com:9092/video_feed"

def main():
    [console.info("STARTING APP..STREET ANALITCS ...") for p in range(10)]
    
    video_capture = cv2.VideoCapture(endpoint)
    # global count

    while True:
        _, frame = video_capture.read()
    
        streamer.update_frame(frame)

        if not streamer.is_streaming:
            streamer.start_streaming()

        cv2.waitKey(30)    

if __name__ == "__main__":
    main()
