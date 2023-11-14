
import tkinter as tk
from tkinter.colorchooser import askcolor #colorchooser module, which will open a modal to select our RGB color combinations


#Functions to make whiteboard work


#Function to start drawing
#event is taken as a parameter. In this case events are actions or occurences(like mouse clicks, key presses) that trigger specific functions when they happen.
#Global variables are accessible from anywhere in the code and can be modified within functions. 

def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y
    #This line captures the current coordinates of the mouse cursor when the start_drawing function is called. It assigns the x and y coordinates of the mouse cursor at that moment to the prev_x and prev_y variables. These variables are used to track the starting point of the drawing action.
    

#Function to draw on whiteboard. 
#Drawing is essentially a combination of points filled with colors, functioning as a vector    
# To work as a vector, it needs to have a starting and ending point.
def draw(event):
    global is_drawing, prev_x,prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = event.x, event.y

#Function to stop drawing after drawing        
def stop_drawing(event):
    global is_drawing
    is_drawing = False
    
#Primary drawing functionality is done

#Color changing features
def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color
        

#Function to adjust the line width, allowing the user to choose thickness of lines.
def change_line_width(value):
    global line_width   
    line_width = int(value)
    

#Use Tkinter to create window for GUI and buttons for choosing colors, clearing whiteboard, and selecting line width.

#Window with title and a white canvas
root = tk.Tk() #creates main application window. Serves as container for all the graphical elements of whiteboard
root.title("Whiteboard") #Create application title of window to "Whiteboard". Appears in title bar

canvas = tk.Canvas(root, bg="White") #creates drawing canvas within main application window. The canvas is a white rectangular area where users can draw. It is initialized with a white background color.
canvas.pack(fill="both", expand=True) #This configures the canvas to fill both the horizontal and vertical space of the application window. It allows the canvas to expand and occupy the entire window.

is_drawing = False
drawing_color = "black"  
line_width = 2 #This initializes a variable line_width to 2. It specifies the width of the lines or strokes used for drawing. The user can adjust this value to change the thickness of the lines.

root.geometry("800x600")  #This sets the initial size of the application window to 800 pixels in width and 600 pixels in height. It defines the dimensions of the window when it is first displayed but you can resize your window and with it, your canvas space.       
            
#Navbar and controls
#Frame to hold the buttons or controls in the same line.
controls_frame = tk.Frame(root)
controls_frame.pack(side = "top", fill="x")       
        
#Button to change color and clear canvas, and give them default fixed positions in your screen

color_button = tk.Button(controls_frame, text="Change Color", command = change_pen_color)
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))

color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)       
        
#Slider to adjust line width
line_width_label = tk.Label(controls_frame, text = "Line Width:")
line_width_label.pack(side="left", padx=5, pady=5)

line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val)) #creates a label widget with the text "Line Width." The label is intended to display text to describe the purpose of the following slider
#line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val)): This line creates a horizontal slider widget (Scale widget) that allows the user to select a line width. The slider ranges from a minimum value of 1 (from_=1) to a maximum value of 10 (to=10). The command option is set to call the change_line_width function with the selected value whenever the slider position changes.
line_width_slider.set(line_width) #This line configures the label's placement within the controls_frame.
#This sets the initial position of the slider to the value stored in the line_width variable, which is initialized earlier in the code. This ensures that the slider starts at the default line width.
line_width_slider.pack(side="left", padx=5, pady=5) 
#side="left": This sets the label to be placed on the left side of the controls_frame. It ensures that the label is aligned to the left.
#padx=5: It adds horizontal padding of 5 pixels around the label, creating some spacing.
#pady=5: It adds vertical padding of 5 pixels around the label, creating spacing.


#Connecting features with the GUI
#Bind the mouse events to the functions that we created earlier. This will ensure that the functions are called whenever the corresponding mouse events occur.

canvas.bind("<Button-1>", start_drawing)
#When the left mouse button is clicked on the canvas, it triggers the start_drawing function.
canvas.bind("<B1-Motion>", draw)
#While the left mouse button is held down and the mouse is moved on the canvas, it triggers the draw function.
canvas.bind("<ButtonRelease-1>", stop_drawing)
#When the left mouse button is released (button released event), it triggers the stop_drawing function.









root = tk.Tk()
print("Tkinter window created")  # This displays a message in the terminal to ensure that the window was created

# Start the Tkinter event loop
root.mainloop()  #In Tkinter, the mainloop() function needs to be called to start the GUI event loop, which handles user inputs and updates the display.      