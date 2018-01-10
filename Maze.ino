#include <Servo.h>
Servo servoRight;
Servo servoLeft;

int LEFTW = 5;
int RIGHTW = 7;



void setup() {
  servoLeft.attach(13);
  servoRight.attach(12);
  pinMode (LEFTW, INPUT);
  pinMode (RIGHTW, INPUT);
}

void forwardServo() {
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(1000);
}
void backwardServo() {
  servoLeft.writeMicroseconds(1000);
  servoRight.writeMicroseconds(2000);
}
void turnLeft() {
  servoLeft.writeMicroseconds(1000);
  servoRight.writeMicroseconds(1000);
}
void turnRight() {
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
}

void loop() {
  if ((digitalRead(LEFTW) == HIGH) && (digitalRead(RIGHTW) == HIGH)) {
    forwardServo();
    delay(500);
  }
  else if ((digitalRead(LEFTW) == LOW) && (digitalRead(RIGHTW) == HIGH)) {
    turnRight();
    delay (500);
  }
  else if ((digitalRead(RIGHTW) == HIGH) && (digitalRead(LEFTW) == LOW)) {
    turnLeft();
    delay (500);
  }
  else if ((digitalRead(LEFTW) == LOW) && (digitalRead(RIGHTW) == LOW)) {
    backwardServo();
    delay (1000);
    turnRight();
    delay (500);
  }
}


