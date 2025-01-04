import lvgl as lv

# App Name
NAME = "Binary Clock"
CAN_BE_AUTO_SWITCHED = True

# LVGL widgets
scr = None
label = None
dot_A1 = None

# Constants

COLOR_RED   = lv.color_hex3(0xF00)
COLOR_GREEN = lv.color_hex3(0x0F0)
COLOR_BLUE  = lv.color_hex3(0x00F)
COLOR_WHITE  = lv.color_hex3(0xFFF)

DEFAULT_FG_COLOR = COLOR_WHITE

DOT_SIZE = 64
DOT_THICKNESS = 12

async def on_start():
    global scr, label, circle

    # Create a new screen object
    scr = lv.obj()

    # Create a style for the circle
    dot_style = lv.style_t()
    dot_style.init()
    dot_style.set_radius(1000)                    # Set radius to create a circle
    dot_style.set_border_width(DOT_THICKNESS)     # Set border width
    dot_style.set_border_color(DEFAULT_FG_COLOR)  # Set border color to white

    # Create an object to represent the circle
    dot_A1 = lv.obj(scr)
    dot_A1.set_size(DOT_SIZE, DOT_SIZE)       # Set size: width and height to 24px
    dot_A1.add_style(dot_style, 0)                # Apply the style to the circle
#     circle.center()                         # Center the circle on the screen

    # Create a label on the screen
    label = lv.label(scr)
    label.set_text("Success!!")

    # Center the label on the screen
    label.align(lv.ALIGN.CENTER, 0, 0)
    label.center()

    # Load the screen
    lv.scr_load(scr)

async def on_running_foreground():
    # This function is called periodically when the app is active
    pass

async def on_stop():
    global scr, label, dot_A1
    # Clean up resources when the app is stopped
    if scr:
        scr.clean()
        scr = None
        label = None
        dot_A1 = None
