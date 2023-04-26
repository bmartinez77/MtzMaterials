# MtzMaterials
MTZ Materials is an embedded web application, scale house system used to emulate weighing semi-trucks. It includes a Raspberry Pi used to host a web application and an Arduino Uno that uses an HX711 module and a load cell sensor. The technologies involved are Python(Flask, SQL-Alchemy, SQLite) and Arduino C. 

## The problem I am Solving
With a shortage of truck drivers, there is a high demand for transporting cargo. With that, it is crucial to keep the trucks within the federal weight limit, of 80,000 pounds or 40 tons. An overloaded truck is dangerous to operate and can cause harm to the roads and other drivers. With a scale house system, this can be prevented, by preventing an order from being completed if the truck is over the weight limit. This will keep the drivers and scale house operators responsible for their weight limit.

## Project Demo
YouTube link: https://www.youtube.com/watch?v=EDEwiAJ6Gdg

## Sample Code
'''  

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
    
'''


## Technologies 
The technologies that are implemented are Raspberry Pi, Arduino, Python(Flask, Jinja, SQLAlchemy), and SQLite. This project implements an MVC architecture.
| Technology or Tool | Version | Justification |
| ------------- | ------------- | ------------- | 
| Raspberry PI 4 | Model B | Raspberry Pi is used to hosut the web application |
| Raspberry Pi OS 64-bit | Debian Version: 11 | Since the application is running on a PI, a PI OS will be used to have a running system. | 
| Python | Version: 3.9.9 | Web Application will be created using python. |
| Flask | Version: 2.2.2 | This is the web framework |
| Jinja | Version 3.1.2 | Jinja is the template engine used for web pages. | 
| SQlAlchemy | Version 2.0.1 | SQlAlchemy is the relational mapper used to store objects in a database and on the web application. |
| Flask-SQlAlchemy | Version 2.0.1 | Flask-SQlAlchemy is used to connect Flask and SQL Alchemy |
| Visual Studio Code | Version 1.61.2 | VS Code is the development tool used to creat and test the web application to host on the Raspberry Pi. |
| Arduin Uno R3 | | The Scale application is hosted on this device and will communicate to the Raspberry Pi. |
| Arduin IDE | 1.8.19 | Used to program and test the arduino. |
| Arduin Programming language |  | Arduino is based off of C/C++, the Arduino will use this language to run its processes |
| GitHub |  | Used as repository to store code. This helped to develop code on laptop and download and test onto the Raspberri Pi.  |
| VNC Viewer |  | Used to remote access to Raspberry Pi. Upload and download files, program and test Arduino and web application |


The technologies to create this project are Raspberry Pi, Arduino, Python, and SQLite. All of these technologies were new to me, I wanted to make a project that used multiple devices that communicate with one another such as the Arduino and the Raspberry Pi. I wanted to implement a physical sensor that is used to be displayed on a web application, where the user can see the change in real time.

## Functional Requirements
The high-level functional requirements are Creating, Reading, Updating, and Deleting orders. Users will be able to create an order using the web application, with the weight that is being read from the scale. The orders will be stored in a database where users will be able to view the orders created. With that, the user is also able to update any order that is in the database. They can change the values for the weight and will be updated in that order. If the user wants to remove an order, they will be able to delete it within the web application. 
| Features | Description |
| ------------- | ------------- |
| Create Order| This features allows users to create and invoice order, they are able to use the weight from the scale to input the gross weight, tare weight, and calculate net weight, and convert it into tons. This order also stores information such as a Truck ID and Name, as well as the Product being used |
| Read Order | Users are able to view all the orders that have been created.   |
| Update Order | Order information can be updated. The user can update the Truck ID, Name, Product, Gross weight and Tare Weight. The Net and Tons will be recalculated when the update has been confirmed  |
| Delete Order | Selected orders can be deleted. These orders weill be removed from the database and cannot be recovered. |

## Non-Functional Requirments
The non-functional requirement implemented in this project is accuracy. This is used to check if the scale is accurate and consistent. The scale will be tested to read within +5% or -5% of the object's weight. If an object is 100 grams, then the accuracy will be tested to see if the scale is reading between 95 grams and 105 grams. 
| Features | Description |
| ------------- | ------------- |
| Accuracy | This feature is for the scales measuerments. We are trying to get +5% or -5% of the true weight of an object |

## Physical Solution 
This is the physical solution that will be used for this project. It shows the circuit used for the Arduino that implments the HX711 module and loadcell sensor. The weight will be displayed on an LCD screen and a potentiometer will allow the back light to the screen to be adjusted. The Arduino is also connected to the Raspberry Pi using a USB cable. 
![physical solution](https://user-images.githubusercontent.com/91274130/234450371-d2f4d688-b35b-4dca-9fe9-bcd004c8319d.png)

When an object is placed onto the load cell, the load cell will have a slight bend, sending an electrical signal to the HX711. The HX711 will then use that signal and convert it into a number for the Arduino to use. 

<img width="553" alt="Screenshot 2023-03-26 at 6 11 01 PM" src="https://user-images.githubusercontent.com/91274130/234463078-8d469a4a-33b3-4134-aed6-7c5e4784b421.png">



## Logical Solution
The logical design explains a high level over view of the project. There are two parts of the application, the web application is connected to the scale using UART protocol over a serial connection. The scale is a separate application working with a physical scale. The Web application will send a request to the Arduino. If it the request is exactly what the Arduino is checking for, it will send a response and reply with the weight to the web application. Where the web application will update the weight on the screen.
![logical design](https://user-images.githubusercontent.com/91274130/234450739-07b067cb-f575-4fbe-a02a-635f51547353.png)

## User Interface Design / Sitemap
User Interface and Site maps are used as a guide for the user to follow the layout and how to navigate through the pages within the web application.
![UI](https://user-images.githubusercontent.com/91274130/234450888-326a7b69-8c04-4662-88d4-6fa5aa883d7e.png)



# Designing the circuit 
A hand drawn schematic was made to outline which pins are connected to fron the arduino to the lcd, potentimeter and the HX711 module. This schematic is helpful when rewiring the circuit and building it on a perfboard.
![IMG-4593](https://user-images.githubusercontent.com/91274130/234453673-d1ca4fac-2495-4a77-b5d5-20f2b08c8642.jpg)

To build the circuit on the perfboard, I created a wire mapping diagram. To start this, I figured out how many holes were on the perfbard, multiplied holes in the rows and columns. Then counted the holes on a piece of grid paper and drew the box. The I wanted to see how the LCD screen and potentiometer needed to be placed to fit in a 3D printed box. Once I was happy with where it was, I marked the holes onto paper to remember where I need to solder the pins into place. 
![IMG-4594](https://user-images.githubusercontent.com/91274130/234453957-2bae1141-6195-45d3-bcc8-17ec0c2f9eb0.jpg)

## Building a prototype
Once the schematic was created, I necided to build a circuit using it. This helped me test the circuit and see if it worked before I build it into a perfboard to keep it permanent. 
![IMG-4596](https://user-images.githubusercontent.com/91274130/234454533-2c6d96b6-2f79-43f9-909b-516a94cb4dec.jpg)


## Building the Project
A perf board was designed to fit inside of a #D printed box used to fit all of the components inside. The perfboard was built off of a breadboard prototype built from the circuit design. This circuit was tested before it was placed into the box. 
![IMG_4487 HEIC](https://user-images.githubusercontent.com/91274130/234452461-1c86d9be-b1df-4012-8c1e-d991914d2c1d.png)

This is the back side of the perfboard. It shows where all the wires are connected to specfic pins. This was built with the mapping diagram.  I decided to have a common power and ground to the perfboard. This allowed me to distribute power from the Arduino to the perfboard. Which connects to the LCD screen, and a resister used fro the brightness, as well distributing power to the HX711 module. As shown by the black (ground) and red (power) cables.
![IMG_4488 HEIC](https://user-images.githubusercontent.com/91274130/234452404-9ff9ad77-8e92-48be-867a-699aee171116.png)


3D printing a box to fit all the components inside. The LCD was measured to see if it is in place to be permanantly stored. This box was designed with Fusino 360 Autodesk and printed using an Creality Ender 3D printer.
![IMG_4489 HEIC](https://user-images.githubusercontent.com/91274130/234452178-b11cf07b-9e72-4eee-9934-b4eac4462cc4.png)

Fitting the Perfboard into the scale box and checking through the back if there is enough room inside to store the other componenets. 
![IMG_4490 HEIC](https://user-images.githubusercontent.com/91274130/234451736-1f764efc-95fa-4940-b8b9-5928b5cc389b.png)

# Final Build
To start the final build, I connected the jumper cables I made with 22 guage stranded wire. I measured then cut the wires to the length I neded for the distance from the perfboard to the Arduino Uno, and HX711 to Aduino. I used a crimping tool for both male and female dupont connectors and crimp pins. The pins were placed at the ends of the wire and crimped into place. Then the housings were slid into place. 
Once the wires were made, I then plugged the wires into the LCD screen pins and glued them so they had more support from being disconnected. 
then the LCD screen had to be placed in the holes. Then I used a hot glue gun to glue the frame of the LCD screen to the box and held it in place til the glue had dried. Then I connected the all the pins from the LCD screen, perfboard and HX711 module to the Arduino. Before placing the Arduino I connected the USB cable in sice it would be difficult to plug it in while stored inside of the box. 
![IMG-4598](https://user-images.githubusercontent.com/91274130/234456635-2c1b498a-b622-4d44-9d2f-dac62abdee49.jpg)

The USB cable was then connected to the Raspberry Pi to test the circuit before storing the Rasbperry Pi inside. A dremel was used to cut holes into the box for the Raspberry Pi to have both the power and HDMI ports a avilable. 
![IMG-4597](https://user-images.githubusercontent.com/91274130/234456584-79ebb44a-951b-44d9-88c5-158561b0df84.jpg)


Both the Arduino and Rasbperry Pi had a 3D printed mount. The initial Idea was to hot glue the mount to be permanently stored inside. This is the full assemble before the power cables has been plugged into the Pi. 
![IMG-4599](https://user-images.githubusercontent.com/91274130/234461542-f6461863-8275-4085-b80d-6904b11b97d6.jpg)

Once the power cable is plugged into the Pi, the Arduino will get power. This will start the code. It will start with its calibration process and using the LCD screen it will let the user know that it is calibrating, then it will say that the scale is ready. Afterwards it will display the weight. 
![IMG-4600](https://user-images.githubusercontent.com/91274130/234461684-0f85b854-4652-4305-930b-3b69167f8bd9.jpg)

This is showing the weight of my headphones when it is placed onto the scale. The scale is not completely accurate since I replaced the 5kg load cell with one that is 20kg. It needs to be recalibrated. 
![IMG-4604](https://user-images.githubusercontent.com/91274130/234462382-3c438460-d4bd-488f-9f0b-eda2810a0d21.jpg)

This is side view with the hole that were cut for the power and HDMI ports for the Pi.
![IMG-4607](https://user-images.githubusercontent.com/91274130/234464132-b7172ca9-6962-43ef-ac0e-18f2025b00bc.jpg)


## Risks and Challenges
One of the risks of this project was that the weight from the scale might have not been able to be sent to the Raspberry Pi through the Arduino. Having a web application is a large process that is running, and adding a sub-process that is used to access the weight from the scale seemed nearly impossible. A sub-process with Python (Flask) will only run before the web application has started. If it is running constantly, the web application will never start. The solution was to leave the design with adding a sub-process and instead use a timed request where the web application is constantly accessing the data from the scale. This is an easier design to manage and gives us the same result we need. 

There were a few challenges, learning how the web application works, how the scale works, creating a circuit design from scratch with no previous experience, and connecting all the components to work together. One of the more technical challenges was managing the communication between the Raspberry Pi and Arduino. 

Using a USB (Universal Serial Bus) cable, the two devices are able to send data back and forth. The issue is that there is a limit to how much data can be sent and stored. Whenever a message is sent, it will be stored in the buffer (a placeholder or slot of memory) and it will not be removed until one of the devices has read or removed it. The initial idea was to constantly send data from the Arduino. But this would fill the buffer and cause data to either leak or for data to be delayed and receive the wrong data. Especially if the Raspberry Pi is not reading the data at the same speed the data is being sent. The solution was for the Raspberry Pi to have a timed request. It will send a message to the Arduino requesting the data, and the Arduino will respond with the weight from the scale. This allows data to be sent when needed and prevents the buffer from overfilling and leaking data, or mistimed data from being sent

Storing all the components inside of the box was a callenge. The components did not fit properly. I had to reorganize the components multiple times to see whcih option was best. The final solution as to keep the LCD screen close to the Arduino and cut holes for the Raspberry Pi ports. This problem would have been minimized if not prevented if the layout was thought of before designing the box.


## Outstanding Issues
One of the outstanding issues is that the web application does not calibrate the scale. The scale must be calibrated before it is used. There is a file that allows the scale to print the resistance value which is then used to calibrate it into a unit of measurement such as grams or pounds.

This project is not ready for production use, we are trying to emulate a scale house since this project does not include scale components for industrial use.

Another issue is transporting the box. Many of the components will move which effect the calibration of the scale. There is a constant need to recalibrate the scale.
