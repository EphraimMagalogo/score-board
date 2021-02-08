score = 0

def on_forever():
    basic.show_number(score)
basic.forever(on_forever)

def on_button_pressed_a():
    global score
    score = 0
    basic.show_number(score)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global score
    score = 4
    basic.show_number(score)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global score
    score += -1
    if score < 0:
        score = score - score
input.on_button_pressed(Button.B, on_button_pressed_b)




