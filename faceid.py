import cv2
import face_recognition
import numpy as np
from tkinter import ttk
from tkinter import*
import pandas as pd
from PIL import Image,ImageTk


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.canvas = Canvas(self.root, width=640, height=480)
        self.canvas.pack()

        window_width = 1530
        window_height = 790
        button_width = 220
        button_height = 40

        x_position = (window_width - button_width) // 2
        y_position = (window_height - button_height) // 2

        b1 = Button(text="start", cursor="hand2", command=self.switch_page)
        b1.place(x=x_position, y=y_position, width=button_width, height=button_height)

    def switch_page(self):
        self.root.withdraw()

        self.new_window = Tk()
        self.new_window.geometry("1530x790+0+0")
        self.new_window.title("Face Denition")

        back_button = Button(self.new_window, text="Back to Main", command=self.back_to_main)
        back_button.pack()

        self.show_webcam()

    def show_webcam(self):
        cap = cv2.VideoCapture(0)

        cap.set(3, 640)
        cap.set(4, 480)

        imgBg = cv2.imread('pictures/R.jpg')

        while True:
          ret, img = cap.read()
          if not ret:
                print("Failed to grab frame from the webcam")
                break
          imgBg[162:162 + 480, 55:55 + 640] = img

          cv2.imshow("Face Detection", imgBg)

  
          if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()  
        cv2.destroyAllWindows()

    def back_to_main(self):
        self.new_window.destroy()
        self.root.deiconify()


if __name__ == "__main__":
   root = Tk()
   obj = FaceRecognitionSystem(root)
   root.mainloop()
    