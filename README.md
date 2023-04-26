# MtzMaterials
MTZ Materials is an embedded web application, scale house system used to emulate weighing semi-trucks. It includes a Raspberry Pi used to host a web application and an Arduino Uno that uses an HX711 module and a load cell sensor. The technologies involved are Python(Flask, SQL-Alchemy, SQLite) and Arduino C. 

## The problem I am Solving
With a shortage of truck drivers, there is a high demand for transporting cargo. With that, it is crucial to keep the trucks within the federal weight limit, of 80,000 pounds or 40 tons. An overloaded truck is dangerous to operate and can cause harm to the roads and other drivers. With a scale house system, this can be prevented, by preventing an order from being completed if the truck is over the weight limit. This will keep the drivers and scale house operators responsible for their weight limit.

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

## Logical Solution
The logical design explains a high level over view of the project. There are two parts of the application, the web application is connected to the scale using UART protocol over a serial connection. The scale is a separate application working with a physical scale. The Web application will send a request to the Arduino. If it the request is exactly what the Arduino is checking for, it will send a response and reply with the weight to the web application. Where the web application will update the weight on the screen.
![logical design](https://user-images.githubusercontent.com/91274130/234450739-07b067cb-f575-4fbe-a02a-635f51547353.png)

## User Interface Design / Sitemap
User Interface and Site maps are used as a guide for the user to follow the layout and how to navigate through the pages within the web application.
![UI](https://user-images.githubusercontent.com/91274130/234450888-326a7b69-8c04-4662-88d4-6fa5aa883d7e.png)

# Building the Project
A perf board was designed to fit inside of a #D printed box used to fit all of the components inside. The perfboard was built off of a breadboard prototype built from the circuit design.
![IMG_4487 HEIC](https://user-images.githubusercontent.com/91274130/234452461-1c86d9be-b1df-4012-8c1e-d991914d2c1d.png)

This is the back side of the perfboard. It shows where all the wires are connected to specfic pins. This was built with the mapping diagram.
![IMG_4488 HEIC](https://user-images.githubusercontent.com/91274130/234452404-9ff9ad77-8e92-48be-867a-699aee171116.png)


3D printing a box to fit all the components inside.
![IMG_4489 HEIC](https://user-images.githubusercontent.com/91274130/234452178-b11cf07b-9e72-4eee-9934-b4eac4462cc4.png)

Fitting the Perfboard into the scale box.
![IMG_4490 HEIC](https://user-images.githubusercontent.com/91274130/234451736-1f764efc-95fa-4940-b8b9-5928b5cc389b.png)


