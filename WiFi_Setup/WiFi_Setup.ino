
#include <SoftwareSerial.h>

SoftwareSerial esp8266(11, 12);
//! Photoresistor Pin
int sensorPin = A0;
//! Storing Sensor Value
int sensorValue = 0;
//! Button pin
int buttpin = 4;
//! Buttonstate
int buttonState;
//! pressed state
int pressed = 0;
//! LEE pin
int ledPin = 3;
//! wifi name
String Wlan = "WebServer";
//! wifi password
String WlanP = "1234567890";
//! ip address
String IP = "192.168.4.2";
//! port
String Port = "3030";

void setup()
{
  Serial.begin(19200);
  pinMode(sensorPin, INPUT);
  pinMode(buttpin, INPUT);
  pinMode(ledPin, OUTPUT);


  Serial.begin(9600);

  esp8266.begin(19200);


  esp8266.println("AT");
  delay(100);
  esp8266.println("AT+CWMODE_CUR=2"); //!Setup
  delay(100);
  esp8266.print("AT+CWSAP_CUR=\"");   //!Setup 2
  esp8266.print(Wlan);
  esp8266.print("\",\"");
  esp8266.print(WlanP);
  esp8266.print("\"");
  esp8266.print(",");
  esp8266.print("5");
  esp8266.print(",");
  esp8266.print("3");
  esp8266.println("");
  delay(500);

}
void wifi() {     //!wifi setup
  if (esp8266.available())
    Serial.write(esp8266.read());
  if (Serial.available())
    esp8266.write(Serial.read());
}

void loop()
{
  wifi();
  buttonState = digitalRead(buttpin); //!Wait for Server to get started
  if (buttonState == HIGH && pressed != 1) {  //!connect to server
    esp8266.print("AT+CIPSTART=\"");
    esp8266.print("TCP");
    esp8266.print("\",\"");
    esp8266.print(IP);
    esp8266.print("\"");
    esp8266.print(",");
    esp8266.print(Port);
    esp8266.println("");
    pressed = 1;
  }
  if (buttonState == 0)//! reset buttonstate
    pressed = 0;


  sensorValue = analogRead(sensorPin);  //! read the value from the sensor
  if (sensorValue <= 500) {
    esp8266.println("AT+CIPSEND=1");
    delay(1000);
    esp8266.println("Z");
    delay(1000);

    if (Serial.available()) {               //!switches LED on or off depending on input from the server
      char serialListener = Serial.read();
      if (serialListener == 'n') {
        digitalWrite(ledPin, HIGH);
      }
      else if (serialListener == 'f') {
        digitalWrite(ledPin, LOW);
      }
    }

  }

}



