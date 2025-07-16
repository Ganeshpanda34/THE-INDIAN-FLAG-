import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Light blue background
screen.title("Indian Flag - Tiranga")
screen.setup(width=900, height=700)

# Create turtle
flag = turtle.Turtle()
flag.speed(0)  # Fastest speed
flag.pensize(2)

# Indian flag colors (exact)
saffron = "#FF9933"
white = "#FFFFFF"
green = "#138808"
navy_blue = "#000080"

# Flag dimensions
flag_width = 400
flag_height = 270
stripe_height = flag_height // 3

# Calculate center position
center_x = 0
center_y = 0

def draw_gradient_background():
    """Draw a subtle gradient background effect"""
    bg_turtle = turtle.Turtle()
    bg_turtle.speed(0)
    bg_turtle.penup()
    bg_turtle.hideturtle()
    
    # Create gradient effect with multiple rectangles
    for i in range(50):
        # Calculate color transition from light blue to very light blue
        blue_intensity = 230 + i // 2
        if blue_intensity > 255:
            blue_intensity = 255
        
        color = f"#{blue_intensity:02x}{blue_intensity:02x}ff"
        bg_turtle.color(color)
        bg_turtle.goto(-450, 350 - i * 14)
        bg_turtle.begin_fill()
        bg_turtle.setheading(0)
        for _ in range(2):
            bg_turtle.forward(900)
            bg_turtle.right(90)
            bg_turtle.forward(14)
            bg_turtle.right(90)
        bg_turtle.end_fill()

def draw_decorative_border():
    """Draw a decorative border around the flag"""
    border_turtle = turtle.Turtle()
    border_turtle.speed(0)
    border_turtle.penup()
    border_turtle.hideturtle()
    
    # Outer decorative border
    border_turtle.goto(-flag_width//2 - 20, flag_height//2 + 20)
    border_turtle.pendown()
    border_turtle.color("#DAA520")  # Golden color
    border_turtle.pensize(4)
    
    # Draw rounded rectangle effect
    for _ in range(2):
        border_turtle.forward(flag_width + 40)
        border_turtle.right(90)
        border_turtle.forward(flag_height + 40)
        border_turtle.right(90)
    
    # Inner shadow effect
    border_turtle.penup()
    border_turtle.goto(-flag_width//2 - 15, flag_height//2 + 15)
    border_turtle.pendown()
    border_turtle.color("#0B3CB8")  # Darker golden color
    border_turtle.pensize(2)
    
    for _ in range(2):
        border_turtle.forward(flag_width + 30)
        border_turtle.right(90)
        border_turtle.forward(flag_height + 30)
        border_turtle.right(90)

def draw_rectangle(x, y, width, height, color):
    """Draw a filled rectangle"""
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

def draw_ashoka_chakra(x, y, radius):
    """Draw the Ashoka Chakra with 24 spokes"""
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color(navy_blue)
    
    # Draw outer circle
    flag.penup()
    flag.goto(x, y - radius)
    flag.pendown()
    flag.pensize(3)
    flag.circle(radius)
    
    # Draw inner circle
    inner_radius = radius * 0.2
    flag.penup()
    flag.goto(x, y - inner_radius)
    flag.pendown()
    flag.begin_fill()
    flag.circle(inner_radius)
    flag.end_fill()
    
    # Draw 24 spokes
    flag.pensize(2)
    for i in range(24):
        angle = i * 15  # 360/24 = 15 degrees per spoke
        
        # Calculate spoke endpoints
        spoke_start_x = x + inner_radius * math.cos(math.radians(angle))
        spoke_start_y = y + inner_radius * math.sin(math.radians(angle))
        spoke_end_x = x + radius * math.cos(math.radians(angle))
        spoke_end_y = y + radius * math.sin(math.radians(angle))
        
        # Draw spoke
        flag.penup()
        flag.goto(spoke_start_x, spoke_start_y)
        flag.pendown()
        flag.goto(spoke_end_x, spoke_end_y)
    
    # Draw small circles at the end of each spoke for smoothness
    flag.pensize(1)
    for i in range(24):
        angle = i * 15
        circle_x = x + radius * 0.9 * math.cos(math.radians(angle))
        circle_y = y + radius * 0.9 * math.sin(math.radians(angle))
        
        flag.penup()
        flag.goto(circle_x, circle_y - 2)
        flag.pendown()
        flag.begin_fill()
        flag.circle(2)
        flag.end_fill()

def draw_corner_decoration(x, y):
    """Draw corner decorations"""
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color("#DAA520")
    flag.pensize(2)
    flag.begin_fill()
    flag.circle(8)
    flag.end_fill()

def draw_flag():
    """Draw the complete Indian flag"""
    # Draw gradient background first
    draw_gradient_background()
    
    # Draw decorative border
    draw_decorative_border()
    
    # Calculate starting position (top-left corner)
    start_x = center_x - flag_width // 2
    start_y = center_y + flag_height // 2
    
    # Draw saffron stripe (top)
    draw_rectangle(start_x, start_y, flag_width, stripe_height, saffron)
    
    # Draw white stripe (middle)
    draw_rectangle(start_x, start_y - stripe_height, flag_width, stripe_height, white)
    
    # Draw green stripe (bottom)
    draw_rectangle(start_x, start_y - 2 * stripe_height, flag_width, stripe_height, green)
    
    # Draw flag border with shadow effect
    # Shadow
    flag.penup()
    flag.goto(start_x + 3, start_y - 3)
    flag.pendown()
    flag.color("#888888")
    flag.pensize(2)
    for _ in range(2):
        flag.forward(flag_width)
        flag.right(90)
        flag.forward(flag_height)
        flag.right(90)
    
    # Main border
    flag.penup()
    flag.goto(start_x, start_y)
    flag.pendown()
    flag.color("black")
    flag.pensize(3)
    for _ in range(2):
        flag.forward(flag_width)
        flag.right(90)
        flag.forward(flag_height)
        flag.right(90)
    
    # Draw Ashoka Chakra in the center
    chakra_radius = stripe_height * 0.4
    chakra_x = center_x
    chakra_y = center_y
    
    draw_ashoka_chakra(chakra_x, chakra_y, chakra_radius)

# Draw the flag
draw_flag()

# Add title with enhanced styling
flag.penup()
flag.goto(0, -220)
flag.pendown()
flag.color("#2C3E50")
flag.write("The Indian National Flag - Tiranga", align="center", font=("Arial", 18, "bold"))

# Add subtitle
flag.penup()
flag.goto(0, -250)
flag.pendown()
flag.color("#34495E")
flag.write("Proud To Be An Indian ", align="center", font=("Arial", 12, "italic"))

# Add corner decorations
draw_corner_decoration(-220, 155)
draw_corner_decoration(220, 155)
draw_corner_decoration(-220, -155)
draw_corner_decoration(220, -155)

# Hide turtle and keep window open
flag.hideturtle()
screen.exitonclick()