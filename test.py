from datetime import datetime as dt 
from datetime import timedelta
import cv2

#import cvlib as cv

# http://insecam.org/en/view/912189/

from console_logging.console import Console
console = Console()

endpoint = "http://ec2-54-91-136-29.compute-1.amazonaws.com:9092/video_feed"

def main():
    [console.info("TESTANDO ENDPOINT ...") for p in range(10)]
    
    video_capture = cv2.VideoCapture(endpoint)
    # global count
    try:
       console.info("INICIANDO TEST.... ") 
       _, frame = video_capture.read()
       console.success(frame)
    except:
       console.error("fail test !")  
if __name__ == "__main__":
    main()