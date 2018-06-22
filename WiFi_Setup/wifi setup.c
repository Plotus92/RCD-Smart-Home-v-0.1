
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
//! LED pin
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
  //!Setup
  esp8266.println("AT+CWMODE_CUR=2"); 
  delay(100);
  //!Setup 2
  esp8266.print("AT+CWSAP_CUR=\"");   
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
//!wifi setup
void wifi() {     
  if (esp8266.available())
    Serial.write(esp8266.read());
  if (Serial.available())
    esp8266.write(Serial.read());
}

void loop()
{
  wifi();
  //!Wait for Server to get started
  buttonState = digitalRead(buttpin); 
  //!connect to server
  if (buttonState == HIGH && pressed != 1) {  
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
  //! reset buttonstate
  if (buttonState == 0)
    pressed = 0;

	//! read the value from the sensor
  sensorValue = analogRead(sensorPin);  
  if (sensorValue <= 500) {
    esp8266.println("AT+CIPSEND=1");
    delay(1000);
    esp8266.println("Z");
    delay(1000);
	//!switches LED on or off depending on input from the server
    if (Serial.available()) {               
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


