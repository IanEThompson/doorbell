/*
 * Doorbell
 * ========
 * when a button is pressed, sends a serial signal saying which on it was. That's all! 
 *  
 */

//define which buttons are connected to which physical pins:
const int btn1=2;
const int btn2=3;
const int btn3=4;
const int btn4=5;
const int btn5=6;
const int btn6=7;
const int btn7=8;
const int btn8=9;
const int btn9=10;
const int LED=13;

void setup() {
  // open the serial port
  Serial.begin(9600);

  //set button pins to input pullup mode (so there is no need for pullup resistors)
  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  pinMode(btn3, INPUT_PULLUP);
  pinMode(btn4, INPUT_PULLUP);
  pinMode(btn5, INPUT_PULLUP);
  pinMode(btn6, INPUT_PULLUP);
  pinMode(btn7, INPUT_PULLUP);
  pinMode(btn8, INPUT_PULLUP);
  pinMode(btn9, INPUT_PULLUP);
  
  //set the LED pin to output mode
  pinMode(LED, OUTPUT);
}

void loop() {
  // just check each button to see which one is pressed
  // if a button is pressed, call the buttonPressed function
  if (digitalRead(btn1)==LOW) buttonPressed(1);
  if (digitalRead(btn2)==LOW) buttonPressed(2);
  if (digitalRead(btn3)==LOW) buttonPressed(3);
  if (digitalRead(btn4)==LOW) buttonPressed(4);
  if (digitalRead(btn5)==LOW) buttonPressed(5);
  if (digitalRead(btn6)==LOW) buttonPressed(6);
  if (digitalRead(btn7)==LOW) buttonPressed(7);
  if (digitalRead(btn8)==LOW) buttonPressed(8);
  if (digitalRead(btn9)==LOW) buttonPressed(9);
}

void buttonPressed(int btn) {
  //turn the LED on, send a serial message, wait a sec then turn the LED off
  digitalWrite(LED, HIGH);
  Serial.println("Button " + String(btn));
  delay(1000);
  digitalWrite(LED, LOW);
}

