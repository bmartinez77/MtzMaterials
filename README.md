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
