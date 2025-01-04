import lvgl as lv

# Name of the App
NAME = "Hello, Dock!"
CAN_BE_AUTO_SWITCHED = True

# Initialize LVGL objects
scr = lv.obj()
label = None
counter = 0

def update_label():
    global counter, label
    # Update the text of the label widget.
    counter += 1
    label.set_text(f'{NAME} {counter}')

async def on_running_foreground():
    # Called when the app is active, approximately every 200ms
    update_label()

async def on_start():
    global label
    # Create and initialize LVGL widgets
    label = lv.label(scr)
    label.center()
    lv.scr_load(scr)
    update_label()

async def on_stop():
    scr.clean()
