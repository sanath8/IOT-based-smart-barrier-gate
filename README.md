# IOT-Based-Barrier-gate
In order to park our vehicles in malls, we would have to get a ticket first from the gate keeper. In case we loose the ticket, it would be troublesome for us to exit the mall. Therefore, this project offers an IOT based solution to this problem. Opencv is used for number plate detection and tesseract is used for registration number extraction from the vehicles.
1) Emty database.
![n1](https://user-images.githubusercontent.com/21198781/38579348-5b65545e-3d24-11e8-822c-239389de0cc7.png)
2) Vehicle enters.
![n2](https://user-images.githubusercontent.com/21198781/38579350-5f20119c-3d24-11e8-88b8-a1f8f6e145fa.png)
3) Extract registration number, if it is not present earlier in database, make a new entry of that vehicle.
![n4](https://user-images.githubusercontent.com/21198781/38579357-64e7b9f4-3d24-11e8-81f2-997444882994.png)
4) Vehicle Leaves and the number plate is captured again.
![n3](https://user-images.githubusercontent.com/21198781/38579354-6232d6c6-3d24-11e8-8975-2727df50f977.png)
5) This time it updates the exit time of that vehicle and also calculates the charge.
![n5](https://user-images.githubusercontent.com/21198781/38579366-67a83a56-3d24-11e8-9bf4-d0dedadd094c.png)


<h2>How to use.</h2>
1) Install opencv and tesseract
2) Run the python file "getRectangle.py"
