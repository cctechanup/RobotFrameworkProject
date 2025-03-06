import subprocess
from pywinauto import Application, keyboard, mouse
from PIL import ImageGrab
import time
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

class AutoCAD:
    def __init__(self):
        self.app = None
        self.acad_window = None

    def ChangeResoultion(self):
        subprocess.run("C:\ROBOTFramework\ACAD_Automation\ChangeResolution.exe 1920x1080", shell=True)

    def open_autocad(self, path_to_autocad):
        """Open AutoCAD application."""
        self.app = Application().start(path_to_autocad)
        time.sleep(5)  # Allow time for AutoCAD to load
        self.acad_window = self.app.window(title_re=".*AutoCAD.*")
        self.acad_window.set_focus()

    def click_at_coordinates(self, x, y):
        """Click on specific screen coordinates."""
        x = int(x)
        y = int(y)
        mouse.click(coords=(x, y))
        mouse.move(coords=(500,50))
        time.sleep(5)
        self.type_command("ribbonclose")
        self.type_command("{ENTER}")

    def type_command(self, command):
        """Type a command in the AutoCAD command line."""
        if not self.acad_window:
            raise Exception("AutoCAD window is not open.")
        self.acad_window.type_keys(command + "{ENTER}")

    def draw_line(self, start_point, end_point):
        """
        Draw a line in AutoCAD.
        :param start_point: Starting point as 'x,y'
        :param end_point: Ending point as 'x,y'
        """
        self.type_command("LINE")
        self.type_command(start_point)
        time.sleep(5)
        self.type_command(end_point)
        self.type_command("{ENTER}")
        self.type_command("")  # Finalize the line command  

    def draw_Circle(self, start_point, diameter):
        self.type_command("CIRCLE")
        self.type_command(start_point)
        time.sleep(5)
        self.type_command(diameter)
        self.type_command("{ENTER}")
        self.type_command("{ENTER}")
        self.type_command("")  # Finalize the line command          
  
    def zoom_extent(self,zoomCommand,extentCommand):
        self.type_command("")
        self.type_command(zoomCommand)
        time.sleep(5)
        self.type_command(extentCommand)   
        self.type_command("{ENTER}")  
        self.type_command("{ESC}") 
        time.sleep(5)
        # self.type_command("")

    def close_autocad(self):
    #"""Close the AutoCAD application."""
        data = {'prodExecutable': 'acad.exe'}
        subprocess.Popen(f"taskkill /F /IM {data['prodExecutable']}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
    
    def resize_autocad(self):
        """Resize AutoCAD window to the upper-left corner of a 1920x1080 screen."""
        # Move and resize to upper-left corner
        self.acad_window.move_window(x=0, y=0, width=960, height=900)  # Half of 1920x1080

    def capture_region(self, x, y, width, height, save_path):
        """Capture a specific screen region."""
        bbox = (int(x), int(y), int(x + width), int(y + height))
        self.img = ImageGrab.grab(bbox=bbox)
        self.type_command("ribbon")
        time.sleep(5)
        self.img.save(save_path)

    def compare_images(self, image1_path, image2_path):
        """
        Compare two images and return the difference percentage.
        """
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)

        # Ensure images have the same size
        if img1.shape != img2.shape:
            print("Images have different sizes.")
            return False

        # Compute absolute difference
        diff = cv2.absdiff(img1, img2)
        non_zero_count = np.count_nonzero(diff)

        # Calculate percentage difference
        total_pixels = diff.size
        diff_percentage = (non_zero_count / total_pixels) * 100

        print(f"Difference: {diff_percentage:.2f}%")
        if(diff_percentage>=5):
            self.close_autocad()
            return diff_percentage
        else:
            return diff_percentage      
        
    
    # def validate_images(self, expected, actual):
    #     self.result = ssim(expected, actual)
    #     if not self.result:
    #         raise AssertionError("Images do not match!")




         
         

