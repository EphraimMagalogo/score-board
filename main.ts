let score = 0
basic.forever(function on_forever() {
    basic.showNumber(score)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    score = 0
    basic.showNumber(score)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    score = 4
    basic.showNumber(score)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    score += -1
    if (score < 0) {
        score = score - score
    }
    
})
