hummingbird.start_hummingbird()

def on_forever():
    hummingbird.set_tri_led(TwoPort.ONE, 255, 87, 51)
    hummingbird.set_tri_led(TwoPort.TWO, 54, 1, 63)
    hummingbird.set_led(ThreePort.ONE, 100)
    hummingbird.set_led(ThreePort.TWO, 100)
    hummingbird.set_led(ThreePort.THREE, 100)
basic.forever(on_forever)
