int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor
int led = 13;
void setup() {
  Serial.begin(19200);
  pinMode(sensorPin, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  sensorValue = analogRead(sensorPin);  // read the value from the sensor
  Serial.println(sensorValue);

  if (sensorValue <= 500) {
    digitalWrite(led, HIGH);
    delay(3000);
    digitalWrite(led, 0);
  }
}
