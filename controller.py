from view import LoginView, SignUpView, ProfileView, END, NORMAL, DISABLED, \
    CreateBidView2, BidsList2View, ContractsList2View
from tkinter import messagebox
from datetime import datetime
from database import DBActions
from model import User

class LoginController:
    """```
        Attributes:
            None
        Short description:
            Initializes the LoginView page and controls it afterwards
    """

    def __init__(self):
        LoginView(self)

    def login_btn2(self, username, password, login):
        """
        Inputs:
            -username: username which was input by the user
            -password: password that was input by the user
            -login: instance of the LoginView view page
        Return: None
        Short description:
             Calls the mechanism that verifies the credential.
             Allows to proceed to the profile page if the credentials are valid.
             Otherwise shows the proper message and allows to reenter credentials
        """
        if username == '' or password == '':
            messagebox.showerror("showerror", "Please fill in all the fields")
            return
        verified_user = DBActions().login(username, password)
        if len(verified_user):
            login.root.destroy()
            verified_user = verified_user[0]
            user = User(verified_user['id'], verified_user['name'], verified_user['username'], verified_user['password'], verified_user['is_seller'])
            ProfileController(user, "Login")
        else:
            messagebox.showerror("showerror", "This account does not exist. Try again")

    def signup_btn(self, view):
        view.root.destroy()
        SignupController()

class SignupController:
    def __init__(self):
        SignUpView(self)

    def signup_btn(self, name, username, password, confirm_password, is_seller, signupview):
        
        user_info = {'name': name, 'username': username, 'password': password, 'is_seller': is_seller}
        
        if password == '' or username == '' or name == '':
            messagebox.showerror("showerror", "Please fill in all the fields")
            return

        if password != confirm_password:
            messagebox.showerror("showerror", "Passwords do not match")
            return
        else:

            user_exist = DBActions().getUserByUsername(username)
            if user_exist:
                messagebox.showerror("showerror", "This account already exists. Try again")
                return
            
            user = DBActions().create_user(user_info)
            if user:
                signupview.root.destroy()
                LoginController()
            else:
                messagebox.showerror("showerror", "This account already exists. Try again")



    def cancel_signup_btn(self, view):
        view.root.destroy()
        LoginController()

class ProfileController:
    """
     Parameters:
         -user: user who is currently logged in to the system
         -initialisation: Indicates where the Profile controller is called from:
            -  "Login": If its called from login page
            - "Back": If its called from other pages

     Short description:
         Initializes the ProfileView page and controls it afterwards, allowing:
            1) Tutor and Student to:
                - log out of the app, redirecting them to LoginView
                - proceed to the ContractsListView to see their existing contracts
            2) Tutor:
                - proceed to the BidsListView page, which will represent all the available for them bids
                - proceed to the OffersBidsListView page, which will represent only the bids that he/she sent an
                offer to
            3) Student:
                - proceed to the BidsListView page, which will represent all their instantiated bids
     """

    def __init__(self, user, initialisation):
        self.user = user
        ProfileView(self.user, self, initialisation)


    def bids_list_btn(self, view):
        view.root.destroy()
        BidsListController(self.user)
        

    def log_out_btn(self, view):
        """
        Inputs:
            - view: instance of the ProfileView page
        Return: None
        Short description:
            Calls the LoginController() which will redirect the user to the LoginView page
        """
        view.root.destroy()
        LoginController()


    def contracts_btn(self, view):
        print('Get contracts for user:', self.user.get_id())
        """
        Inputs:
            - view: instance of the ProfileView page
        Return: None
        Short description:
            Calls the ContractsListController() which will redirect the user to the ContractsListView page
        """
        view.root.destroy()
        ContractsListController(self.user)


class BidsListController:
    """
    Attributes:
        -user: user who is currently logged in to the system
        -bids: up-to-date bids that - are initiated by the student if the user is the Student
                                    - are available for the tutor based on his competency if the user is Tutor

    Short description:
        Initializes the BidsList page calling the GetBids() class to sort out the bids to represents and Controls the page
        by responding to the user input (clicking buttons, etc)
    """

    def __init__(self, user):
        self.user = user
        is_seller = self.user.get_is_seller()

        bids = []
        if is_seller == 'Seller':
            bids = DBActions().getMyBids(self.user.get_id())
        else:
            bids = DBActions().getAllBids(1)

        print('bids------', bids)
        if bids is None:
            self.bids = []
        else:
            self.bids = bids
            
        BidsList2View(self, self.bids, self.user)

    def approve_bid_btn(self, view, selected_bid):

        print('Approve bid for bid id: ', selected_bid)
        
        contract = {
            'buyer': self.user.get_id(),
            'seller': selected_bid['initiator'],
            'bid_id': selected_bid['id'],
            'date_created': datetime.now(),
            'date_signed': datetime.now(),
            'status': 1
        }

        result = DBActions().createContract(contract)
        if result:
            view.root.destroy()

            DBActions().updateBidStatus(selected_bid['id'], 2)
            ProfileController(self.user, "Back")
        else:
            messagebox.showerror("showerror", "Error creating bid, try again")

    def create_bid_btn(self, view):
        """
        Inputs:
            - view: instance of the BidsListView page
        Return: None
        Short description:
            Checks whether the student is not exceeding their limit on
            bids and contracts, restricting it to the maximum number of bids = 5 - number of existing
            contracts.
            If student is exceeding the limit an error message will appear else the student will be redirected to
            ChooseBidView.
        """
        view.root.destroy()
        CreateBidController(self.user, 'open')


    def back_btn(self, view):
        """
        Inputs:
            - view: instance of the BidsListView page
        Return: None
        Short description:
            Calls the ProfileController which will redirect the user to the ProfileView page
        """
        view.root.destroy()
        ProfileController(self.user, "Back")


class CreateBidController:
    """
    Parameters:
        -user: user who is currently logged in to the system
        -type_bid: type of the bid to be created

    Attributes:
        -CreateBidView: page that is being created and controlled by this controller class

    Short description:
        Initializes the CreateBidView page based on the type of the bid that user has chosen and controls it afterwards.
        Creates new bid, based on all the information that the user input by calling the BidCreator class and
        passing the bid type there.
    """

    def __init__(self, user, type_bid):
        self.user = user
        self.type_bid = type_bid
        CreateBidView2(self, user, 'Open')

    def submit_form(self, item_name, item_descption, quantity, amount, user_id, selected_date, view):
        """
        Inputs:
            - bid_info: Information regarding the bid created
            - lesson_info: Information regarding the lesson required by bid creator
            - view: instance of the CreateBidView page
        Return: None
        Short description:
            Gets all the data that was input by the student to create the bid and formats it properly.
            Calls the BidCreator passing the bid type and formatted data and redirects the user back to the
            BidListView page
        """
        # validate name, quantity, amount should not be null

       
        if item_name == '' or item_descption == '' or quantity == '' or amount == '':
            messagebox.showerror("showerror", "Product name, quantity and amount should not be empty")
            return

        close_date = datetime.strptime(selected_date, '%Y, %m, %d')
        
        bid = {
            'initiator': user_id,
            'item': item_name,
            'description': item_descption,
            'date_created': datetime.now(),
            'amount': amount,
            'quantity': quantity,
            'date_closed': close_date,
        }


        res = DBActions().createBid(bid)
        if res:
            print('Bid created successfully')
            view.root.destroy()
            BidsListController(self.user)
        else:
            messagebox.showerror("showerror", "Error creating bid, try again")

    def cancel_btn(self, view):
        print
        """
        Short description:
            1) destroys CreateBidView
            2) redirects the user to the BidslistView """
        view.root.destroy()
        BidsListController(self.user)


class ContractsListController:
    """
    Attributes:
        -user: user who is currently logged in to the system
    Short description:
        Responsible for Contract related operations :
        - allows the user to see the contracts sorted by:
            - ongoing (signed and not expired)
            - expired (signed but expired)
            - pending (the contract request sent ny the student to the tutor), which isnt signed by the tutor yet
        - back_btn: Sends the user back to their profile page
    """

    def __init__(self, user):
        self.user = user
        contracts = DBActions().getContract(self.user.get_id())
        if contracts is None:
            self.contracts = []
        else:
            self.contracts = contracts

        ContractsList2View(self, self.contracts)


    def back_btn(self, view):
        """
        Short Description:
            1) Closes the view which the user is in
            2) Redirects the user to the Profile page
        :param view: Instance of contractsListView
        :return: None
        """
        view.root.destroy()
        ProfileController(self.user, "Back")


# start of the app
if __name__ == "__main__":
    LoginController()
