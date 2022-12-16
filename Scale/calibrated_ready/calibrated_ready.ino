// Arduino, HX711 module, and LCD Library
#include <Arduino.h>
#include "HX711.h"
#include <LiquidCrystal.h>

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

// creating scale object used in the header file
HX711 scale;

// creating lcd screen to diplay weight
LiquidCrystal lcd(4, 6, 10, 11, 12, 13);

// setup code used at start up
// allows the scale to calibrate itself before a weight is placed on the scale
void setup() {
  // baud rate used for the communication speed
  Serial.begin(115200);
  Serial.println("Initializing the scale");

  // setting up scale pins 
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);  

  Serial.println("Before setting up the scale:");
  
  Serial.print("read: \t\t");
  // print a raw reading from the ADC
  Serial.println(scale.read());      

  Serial.print("read average: \t\t");
  // print the average of 20 readings from the ADC
  Serial.println(scale.read_average(20));   

  Serial.print("get value: \t\t");
  // print the average of 5 readings from the ADC minus the tare weight (not set yet)
  Serial.println(scale.get_value(5));   

  Serial.print("get units: \t\t");
  // print the average of 5 readings from the ADC minus tare weight (not set) divided
  Serial.println(scale.get_units(5), 1);  
  
  // setting calibration factor used to calibrate the scale. Value is from uncalibrated program            
  scale.set_scale(378.92);
  //scale.set_scale(-471.497);// this value is obtained by calibrating the scale with known weights

  // reset the scale to 0
  scale.tare();       
          
  Serial.println("After setting up the scale:");

  Serial.print("read: \t\t");
  // print a raw reading from the ADC
  Serial.println(scale.read());

  Serial.print("read average: \t\t");
  // print the average of 20 readings from the ADC
  Serial.println(scale.read_average(20));       

  Serial.print("get value: \t\t");
  // print the average of 5 readings from the ADC minus the tare weight, set with tare()
  Serial.println(scale.get_value(5));   

  Serial.print("get units: \t\t");
  // print the average of 5 readings from the ADC minus tare weight, divided
  Serial.println(scale.get_units(5), 1);
          
  // by the SCALE parameter set with set_scale
  Serial.println("Readings:");
}


void loop() {
  // clear data on LCD screen 
  lcd.clear();
  // sets the cursor to the first index, allowing data to be placed ath the beginning
  lcd.setCursor(0,0);
  // printing the value of one reading
  lcd.print(scale.get_units(), 1);
  
  Serial.print("one reading:\t");
  // print one value
  Serial.print(scale.get_units(), 1);
  
  Serial.print("\t| average:\t");
  // print the average value
  Serial.println(scale.get_units(10), 5);

  // time delay
  delay(5000);
}
