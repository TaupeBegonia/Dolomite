import tkinter as tk
import datetime
import math

# All states that tax period products
states_tax_dict = {"AL": 0.04, "AZ": 0.056, "AR": 0.065, "GA": 0.04,
                   "HI": 0.04, "ID": 0.06, "IN": 0.07, "KS": 0.0615,
                   "KY": 0.06, "MS": 0.07, "MO": 0.04225, "NC": 0.0475, 
                   "ND": 0.05, "OK": 0.045, "SC": 0.06, "SD": 0.04, 
                   "TN": 0.07, "TX": 0.0625, "UT": 0.07, "WV": 0.06, 
                   "WI": 0.05, "WY": 0.04}



# Define the application class
class CostCalcApp:
    
    def __init__(self):
        
        # Instantiate a tkinter GUI window
        self.main = tk.Tk()
        self.main.title("Menstrual Product Lifetime Cost Calculator in the US")
        self.main.geometry('650x500')
        
        # Add the questions
        self.add_labels()
        
        
        # Textboxes in the form
        # for some reason I have to separate the textbox creation and placement
        self.cycle_len_txt = tk.Entry(self.main)
        self.cycle_len_txt.place(x = 400, y = 50)

        self.period_len_txt = tk.Entry(self.main)
        self.period_len_txt.place(x = 400, y = 75)

        self.num_daily_txt = tk.Entry(self.main)
        self.num_daily_txt.place(x = 400, y = 100)

        self.num_pack_txt = tk.Entry(self.main)
        self.num_pack_txt.place(x = 400, y = 125)

        self.pack_cost_txt = tk.Entry(self.main)
        self.pack_cost_txt.place(x = 400, y = 150)


        self.start_input_txt = tk.Entry(self.main)
        self.start_input_txt.place(x = 400, y = 200)

        self.end_input_txt = tk.Entry(self.main)
        self.end_input_txt.place(x = 400, y = 225)


        self.state_txt = tk.Entry(self.main)
        self.state_txt.place(x = 400, y = 275)

        self.inflation_txt = tk.Entry(self.main)
        self.inflation_txt.place(x = 400, y = 325)
        
        
        # The submit button
        tk.Button(self.main, text="Submit", command = self.calculate).place(x = 425, y = 350)
        
        
        # Calculation message that appears at bottom, initially empty
        self.calculation_label = tk.StringVar(self.main, "")
        tk.Label(self.main, textvariable=self.calculation_label).place(x=100, y=425)
        
        
        # Create and display the menu bar
        self.menubar = tk.Menu(self.main)
        self.add_menus(self.menubar)
        self.main.config(menu=self.menubar)
        
        
    def run(self):
        """
        Run the app

        Returns
        -------
        None.

        """
        self.main.mainloop()
        
        
        
    def add_labels(self):
        """
        Add form questions

        Returns
        -------
        None.

        """
        tk.Label(self.main, text = "What is your menstrual cycle length in days?").place(x = 100, y = 50)
        tk.Label(self.main, text = "What is your period length in days?").place(x = 100, y = 75)
        tk.Label(self.main, text = "How many sanitary products do you use per day?").place(x = 100, y = 100)
        tk.Label(self.main, text = "How many sanitary products are there per package?").place(x = 100, y = 125)
        tk.Label(self.main, text = "How much does each package cost?").place(x = 100, y = 150)

        tk.Label(self.main, text = "Enter your start date (year/month/day):").place(x = 100, y = 200)
        tk.Label(self.main, text = "Enter your end date (year/month/day):").place(x = 100, y = 225)

        tk.Label(self.main, text = "What US state do you live in (abbreviation)?").place(x = 100, y = 275)
        tk.Label(self.main, text = "(Leave blank if you do not want to include sales tax)").place(x = 100, y = 295)
        tk.Label(self.main, text = "What is your yearly expected inflation rate (percent)?").place(x = 100, y = 325)
        tk.Label(self.main, text = "(Leave blank if you do not want to include inflation)").place(x = 100, y = 345)
        
        
        
    def add_menus(self, menubar):
        """
        Add menu options to the menubar

        Parameters
        ----------
        menubar : tkinter menubar
            an empty menubar

        Returns
        -------
        None.

        """
        # Create the File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Close", command=self.main.destroy)
        file_menu.add_command(label="Clear All", command=self.clear)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_command(label="Load", command=self.load)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create the Plot menu
        plot_menu = tk.Menu(menubar, tearoff=0)
        plot_menu.add_command(label="Plot Graph", command=self.plot)
        menubar.add_cascade(label="Plot", menu=plot_menu)
        
        # Create the Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=help_menu)


    def about(self):
        """
        Shows a messagebox about this app

        Returns
        -------
        None.

        """
        tk.messagebox.showinfo("About this app", "This is the Menstual Product Lifetime Cost Calculator")
        
        
        
    def clear(self):
        """
        Clears all textboxes

        Returns
        -------
        None.

        """
        
        self.cycle_len_txt.delete(0,'end')
        self.period_len_txt.delete(0,'end')
        self.num_daily_txt.delete(0,'end')
        self.num_pack_txt.delete(0,'end')
        self.pack_cost_txt.delete(0,'end')
        self.start_input_txt.delete(0,'end')
        self.end_input_txt.delete(0,'end')
        self.state_txt.delete(0,'end')
        self.inflation_txt.delete(0,'end')


    def save(self):
        """
        Save the textbox values in a .csv file

        Returns
        -------
        None.

        """
        pass
    
    
    def load(self):
        """
        Load in values from a .csv file into the textboxes

        Returns
        -------
        None.

        """
        pass
    
    
    
    def plot(self):
        """
        Plots a graph based on values in a new window

        Returns
        -------
        None.

        """
        # Create a new window for the plot
        new_plot = tk.Tk()
        new_plot.title("The Plot")
        new_plot.geometry("300x300")
        
        new_plot.mainloop()



    def calculate(self):
        """
        Takes the user inputs and calculates the 
        total lifetime cost for menstrual products 
        
        Shows the cost at the window bottom

        Returns
        -------
        None.

        """
        
        try:
            
            # Get all the user inputs
            cycle_len = int(self.cycle_len_txt.get())
            period_len = int(self.period_len_txt.get())
            num_daily = int(self.num_daily_txt.get())
            num_per_pack = int(self.num_pack_txt.get())
            pack_cost = int(self.pack_cost_txt.get())

            start_input = self.start_input_txt.get()
            end_input = self.end_input_txt.get()

            state = self.state_txt.get().upper()
            inflation_rate = self.inflation_txt.get()

            start_list = start_input.split('/')
            end_list = end_input.split('/')

            start_date = datetime.date(int(start_list[0]), int(start_list[1]), int(start_list[2]))
            end_date = datetime.date(int(end_list[0]), int(end_list[1]), int(end_list[2]))


            # Start crunching the numbers
            
            
            # create a timedelta object
            diff = end_date - start_date

            #print()
            #print("There are", diff.days, "days between", start_date, "and", end_date)

            # calculate the total number of menstrual cycles
            num_cycles = diff.days // cycle_len

            # calculate the number of years between the dates
            num_years = diff.days // 365

            # calculate the total number of days where a period is present in a lifetime
            total_period_days = num_cycles * period_len

            # calculate the total menstrual products used in a lifetime
            total_products_used = total_period_days * num_daily

            # calculate the total packages of period products used in a lifetime
            total_packages_used = math.ceil(total_products_used / num_per_pack)

            # calculate the cost of all those packages.
            gross_cost = total_packages_used * pack_cost

            # calculate tax
            if state:
                if state in states_tax_dict:
                    net_cost = gross_cost * (1 + states_tax_dict[state])
                else:
                    net_cost = gross_cost
            else:
                net_cost = gross_cost

            #calculate inflation
            if inflation_rate:
                inflation_decimal = float(inflation_rate) * 0.01
                total_cost = net_cost * (1 + inflation_decimal)**num_years
                sentence = f"The total cost of your period is about ${total_cost:.2f}, with inflation."
            else:
                sentence = f"The total cost of your period is about ${net_cost:.2f}, without inflation."
            
            
            # Calculation appears beneath submit button
            self.calculation_label.set(sentence)
            
        
        
        # If the user inputs anything wrong (strings for ints, etc)
        except:
            self.calculation_label.set("There was an error in your inputs. Try again!")
            #tk.messagebox.showinfo("Error!", "There was an error in your inputs. Try again!")

      


# Run the program
if __name__ == "__main__":
    window = CostCalcApp()
    window.run()

