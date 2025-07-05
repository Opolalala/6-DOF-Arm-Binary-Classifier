#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

const int SERVOMIN = 150;
const int SERVOMAX = 600;

const int baseChannel = 0;
const int shoulderChannel = 1;
const int elbowChannel = 3;
const int wrist1Channel = 4;
const int wrist2Channel = 6;
const int gripperChannel = 7;

int angleToPulse(int angle) {
  return map(angle, 0, 180, SERVOMIN, SERVOMAX);
}

void moveToAngles(int base, int shoulder, int elbow, int wrist1, int wrist2, int gripper) {
  pwm.setPWM(baseChannel, 0, angleToPulse(base));
  delay(300);
  pwm.setPWM(shoulderChannel, 0, angleToPulse(shoulder));
  delay(300);
  pwm.setPWM(elbowChannel, 0, angleToPulse(elbow));
  delay(300);
  pwm.setPWM(wrist1Channel, 0, angleToPulse(wrist1));
  delay(300);
  pwm.setPWM(wrist2Channel, 0, angleToPulse(wrist2));
  delay(300);
  pwm.setPWM(gripperChannel, 0, angleToPulse(gripper));
  delay(300);
}
void movewrist1(int wrist1) {
  pwm.setPWM(wrist1Channel, 0, angleToPulse(wrist1));
  delay(1000);
}
void movebase(int base) {
  pwm.setPWM(baseChannel, 0, angleToPulse(base));
  delay(1000);
}
void moveshoulder(int shoulder) {
  pwm.setPWM(shoulderChannel, 0, angleToPulse(shoulder));
  delay(1000);
}
void moveelbow(int elbow) {
  pwm.setPWM(elbowChannel, 0, angleToPulse(elbow));
  delay(1000);
}


void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(50); // Standard for servos

  delay(1000);

  Serial.println("Moving...");
  
  
    
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    
    if (command == 'r') {
      moveToAngles(70,30,20,80,15,10); 
      delay(1000);
      movebase(80);
      delay(2000);
      moveshoulder(60);
      delay(1000);
      moveelbow(17);
      movebase(50);
    } 
    else if (command == 'g') {
      moveToAngles(70,30,20,80,15,10); 
      delay(1000);
      //orange
      movebase(60);
      delay(2000);
      moveshoulder(60);
      delay(1000);
      moveelbow(17);
      movebase(90);      
    }
  }
  delay(100);
}