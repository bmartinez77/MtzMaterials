// Calibrating the load cell
#include "HX711.h"
#include <LiquidCrystal.h>// include the library code

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

// creating scale object used in the header file
HX711 scale;

// creating lcd screen to diplay weight
LiquidCrystal lcd(4, 6, 10, 11, 12, 13);


void setup() {
  // put your setup code here, to run once:
  // baud rate used for the communication speed
  Serial.begin(9600);
  
  // setting up scale pins 
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);  
}

void loop() {
  // put your main code here, to run repeatedly:
// checks if there an item has been placed onto the scale
  if (scale.is_ready()) {
    
    // sets scale allows it to be calibrated with no weight, 
    scale.set_scale();    
    Serial.println("Tare... remove any weights from the scale.");
    delay(5000);
    
    // resets the scale
    scale.tare();
    
    Serial.println("Tare done...");
    Serial.print("Place a known weight on the scale...");
    delay(5000);

    // value used to get the average f 10 measurements, 
    long reading = scale.get_units(10);

    // print results on serial
    Serial.print("Result: ");
    Serial.println(reading);

    // restes the lcd screen and displays value 
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print(reading);
    
  } 
  else {
    // error handling if a scale is not found
    Serial.println("HX711 not found.");
  }
  delay(1000);
}
//calibration factor will be the (reading)/(known weight), value used int calibrated code.
