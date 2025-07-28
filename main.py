def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global receivedString
    receivedString = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    if receivedString == "Forward":
        basic.show_arrow(ArrowNames.NORTH)
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 20)
        basic.pause(500)
        maqueen.motor_stop(maqueen.Motors.ALL)
    elif receivedString == "Backward":
        basic.show_arrow(ArrowNames.SOUTH)
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 20)
        basic.pause(500)
        maqueen.motor_stop(maqueen.Motors.ALL)
    elif receivedString == "Left" or receivedString == "Turn-Left":
        basic.show_arrow(ArrowNames.WEST)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 20)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
        basic.pause(500)
        maqueen.motor_stop(maqueen.Motors.ALL)
    elif receivedString == "Right" or receivedString == "Turn-Right":
        basic.show_arrow(ArrowNames.WEST)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 20)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 20)
        basic.pause(500)
        maqueen.motor_stop(maqueen.Motors.ALL)
    elif receivedString == "Sound":
        music.play(music.string_playable("E G B A B C5 B C5 ", 250),
            music.PlaybackMode.UNTIL_DONE)
    elif receivedString == "Talk":
        music.play(music.create_sound_expression(WaveShape.TRIANGLE,
                3328,
                2494,
                255,
                255,
                1500,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
    basic.pause(500)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

receivedString = ""
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)