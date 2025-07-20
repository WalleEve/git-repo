#include <Servo.h>  // Include the Servo library

Servo myServo;  // Create a Servo object

int servoPin = 9;  // Define the pin the servo is connected to

void setup() {
  myServo.attach(servoPin);  // Attach the servo to the defined pin
}

void loop() {
  // Wait for 60 seconds (60000 milliseconds)
  delay(6000);  

  // Turn the servo to 90 degrees
  myServo.write(360);  
  delay(1000);  // Wait for 1 second

  // Return the servo back to 0 degrees
  myServo.write(0);  
  delay(1000);  // Wait 1 second before repeating the cycle
}
