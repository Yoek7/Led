import time

# Replace with the appropriate PWM pin number
pwm_pin_number = 18

# Set the buzzer frequency (in Hz)
buzzer_frequency = 1000

# Initialize PWM
pwm = PWM(pwm_pin_number)
pwm.frequency = buzzer_frequency

# Set the duty cycle to 50% to turn on the buzzer
pwm.duty_cycle = 0.5
pwm.enable()

# Keep the buzzer on for 1 second
time.sleep(1)

# Turn off the buzzer
pwm.duty_cycle = 0
pwm.enable()

# Close the PWM pin
pwm.close()