# Park Pilot
Park Pilot with audible alerts, made with Python and Arduino.

In this project, it was used an Arduino UNO and an Ultrasonic Sensor HC-SR04 to measure the ping. To read the Serial Port, it was used pySerial and to develop the Park Pilot interface it was used Pygame. The main objective is to make the most of the data acquired from the Arduino code, translating the data that are hard to visualize into a reasonable understanding of the distance between the sensor and an object. Thereunto, it was constructed a virtual scenario of a car moving, proportionally with the distance, in a parking lot with beep sounds to alert the driver, with Python code.

<img src="https://user-images.githubusercontent.com/78885092/129488446-79b953eb-2bbb-481b-800d-a6ee0e0b35d0.jpeg" width="33%" height="33%">
<img src="https://user-images.githubusercontent.com/78885092/129488390-cd53afb4-9811-405d-a506-f99a3a13d385.png" width="65%" height="65%">

When the distance is too far, the program displays a waiting background.

<img src="https://user-images.githubusercontent.com/78885092/129501118-0dfd29ff-e4e5-4cf3-9bb4-009604a590f2.png" width="40%" height="40%">

There is 4 beep sounds with different BPM to indicate how close the sensor is of the object.

<img src="https://user-images.githubusercontent.com/78885092/129501129-f35007f9-4b6e-4836-99c7-1e811d19bcee.png" width="40%" height="40%">

The animation needs to be improved, there are still some unwanted flicks and the animation will look smoother after some adjustments that I'm working on.
