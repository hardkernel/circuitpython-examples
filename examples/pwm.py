import pwmio
import board

pwm = pwmio.PWMOut(board.D15)

while True:
    for cycle in range(0, 65535):
        pwm.duty_cycle = cycle
    for cycle in range(65534, 0, -1):
        pwm.duty_cycle = cycle
