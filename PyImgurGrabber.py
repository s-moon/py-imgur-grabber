from datetime import datetime
import time
import pyimgur
import pyperclip
import subprocess

# constants
CLIENT_ID = "d9dffbb99f26248"
SCREEN_GRABBER = "C:\\PyImgurGrabber\\bin\\MiniCap.exe"

# filename
basename = "C:\\MiniCap\\imgur"
suffix = datetime.now().strftime("%y%m%d_%H%M%S")
extension = ".jpg"
JPG_PATH = "_".join([basename, suffix, extension]) # e.g. 'imgur_120508_171442.jpg'

# run the screen grabber
subprocess.call([SCREEN_GRABBER, "-captureregselect", "-exit", "-save", JPG_PATH])

# upload the image saved
im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(JPG_PATH, title="ScreenShot by PyImgurGrabber")
print("URL:", uploaded_image.link, "Size:", uploaded_image.size)

# place imgur url into clipboard so that we can paste it somewhere
pyperclip.copy(uploaded_image.link)

# sleep for 15 seconds
time.sleep(15)

# now delete image
print ("Deleting " + uploaded_image.link)
uploaded_image.delete()