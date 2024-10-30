# Description 
The application is an online bidding system to buy or sell products. 
Users whose accounts exist in the this system are allowed to login into the application using their username and the respective password. The account is initially assigned a role, so that the user will be immediately logged in with their respective role: __seller__ or __buyer__. 

### Seller
The student can create bids. Bids created by the Seller will be shown to all the Buyers. 

### Buyer
The buyer can see bids and can accept the bids.


### Contract
- both Buyer and Sellerors have a list of contracts


# Development
The application was developed in Python with Tkinter GUI toolkit. The main goal of this project was to not just create a working system,
but to ensure that the application is developed in an object oriented programming model utilizing various object oriented principles.

### Running the application
      pip install requirements.txt
      python controller.py

### DB Setup
      Create DB using migrations queries.
      Update DB credentials in database.py
