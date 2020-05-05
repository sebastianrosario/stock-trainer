# stock-trainer
A virtual investor where you get to choose the stocks and the volume of your portfolio. Made with Python.
Draft 1 - Stock Trainer

Create an interaction between the python program and stock market data through Alpha Vantage API so that the user can follow a specific stock, virtually invest in it, see their change and other data about it. 

Goals: Allow user to virtually invest how ever much money they want into a specific stock to see how much they would yield in a certain day. 

Stretch Goals: Allow multiple portfolios of different stock data, kind of like save files. 

Super Stretch Goals: Add in recommendations for stock to invest in. 
Scope: Allow user interaction through a command line, asking for input from the user for the code to calculate investments from day to day. 


2/16 Hello World!

2/23 Pick a stock API

3/1 Find a way to implement the API into to the Python Project

3/8 Parse API data, to take things that are relevant. 

3/15 Manipulate stock data from API 

3/22 Save the net gains from each day 

3/29 Analyze net gains from single stock from each consecutive day 

4/5 Have the program make the save files if it is the first launch (if statements)

4/12 Conveniently store and recall stock symbols and stock volume from user (linked list? array?)

4/19 Variable persistence using files created by the code

4/26 Make user input prompts more readable and easier to use 


Milestone 1: Get stock data into Python project. 

Milestone 2: Saving the progress each day.

Milestone 3: Saving variables from each launch

Milestone 4: Saving stock symbols and stock volume from user input, usable on next launch

App Explanation: The app starts by checking if the user has run the app before. This is done by checking if the file that the app creates on launch exists or not. It then prompts the user for a stock symbol and a stock volume which is saved between launches. The app then calls the stock API to retrieve the opening and closing price of the selected stock and sends that to a file called "Dayrate.txt". After the user has opened the application once, it no longer asks for the stock symbol or volume as it is saved and reloaded by using pickle. The daily calculations execute and the program ends. 
