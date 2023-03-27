// Arduino, HX711 module, and LCD Library
#include <Arduino.h>
// scale module
#include "HX711.h"
// LCD header file
#include <LiquidCrystal.h>
// JSON header file used for JSON data transmission
#include <ArduinoJson.h>


// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

// creating scale object used in the header file
HX711 scale;

// Creates an LCD object. Parameters: (rs, enable, d4, d5, d6, d7)
// creating lcd screen to diplay weight
LiquidCrystal lcd(6, 7, 10, 11, 12, 13);

// setup code used at start up
// allows the scale to calibrate itself before a weight is placed on the scale
void setup() {
  // baud rate used for the communication speed
  Serial.begin(9600);

  // setting up scale pins 
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);  
  // remove text from screen
  lcd.clear();
  // set cursor, where to start the message
  lcd.setCursor(0,0);
  // printing mesage on lcd screen
  lcd.print("Calibrating Scale Please wait:");
  // setting calibration factor used to calibrate the scale. Value is from uncalibrated program            
  scale.set_scale(-378.92);
  //scale.set_scale(-471.497);// this value is obtained by calibrating the scale with known weights

  // reset the scale to 0
  scale.tare();       

  // timed delay
  delay(3000);
  // clear lcd screen
  lcd.clear();
  // reset cursor
  lcd.setCursor(0,0);
  
  // printing the value of one reading
  lcd.print("Scale is ready please place a weight");
  // time delay
  delay(2000);
}


void loop() {
  // clear data on LCD screen 
  lcd.clear();
  // sets the cursor to the first index, allowing data to be placed ath the beginning
  lcd.setCursor(0,0);
  // printing the value of one reading
  lcd.print(scale.get_units(), 1);

  // for loop checking if a message has been sent
   if (Serial.available() > 0) {
    // read message
      String message = Serial.readStringUntil('\n');

      // if message is true
      if(message == "on"){
        // initialize json messafe
        StaticJsonDocument<200> doc;

        // set message value to weight of from scale
        doc["value"] = scale.get_units();
        // send message to serial port
        serializeJson(doc, Serial);
    }
   }
  // time delay
  delay(1000);
}
