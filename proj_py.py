import tkinter as tk
import datetime
import math

# All states that tax period products
states_tax_dict = {"AL": 0.04, "AZ": 0.056, "AR": 0.065, "GA": 0.04, "HI": 0.04, "ID": 0.06,
                   "IN": 0.07, "KS": 0.0615, "KY": 0.06, "MS": 0.07, "MO": 0.04225, "NC": 0.0475,
                   "ND": 0.05, "OK": 0.045, "SC": 0.06, "SD": 0.04, "TN": 0.07, "TX": 0.0625,
                   "UT": 0.07, "WV": 0.06, "WI": 0.05, "WY": 0.04}

# Create the tkinter GUI
window = tk.Tk()
window.title("Menstrual Product Lifetime Cost Calculator in the US")
window.geometry('700x500')


def calculate():
    """
    Takes the user inputs and calculates the 
    total lifetime cost for menstrual products 
    
    Shows the cost in a message box

    Returns
    -------
    None.

    """
    try:
        mens_len = int(a1.get())
        per_len = int(b1.get())
        num_daily = int(c1.get())
        num_per_pack = int(d1.get())
        pack_cost = int(e1.get())

        start_input = f1.get()
        end_input = g1.get()

        state = h1.get().upper()
        inflation_rate = i1.get()

        start_list = start_input.split('/')
        end_list = end_input.split('/')

        start_date = datetime.date(int(start_list[0]), int(start_list[1]), int(start_list[2]))
        end_date = datetime.date(int(end_list[0]), int(end_list[1]), int(end_list[2]))

        # create a timedelta object
        diff = end_date - start_date

        #print()
        #print("There are", diff.days, "days between", start_date, "and", end_date)

        # calculate the total number of menstrual cycles
        num_cycles = diff.days // mens_len

        # calculate the number of years between the dates
        num_years = diff.days // 365

        # calculate the total number of days where a period is present in a lifetime
        total_period_days = num_cycles * per_len

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
        
        tk.messagebox.showinfo("Calculator Result", sentence)
    
    except:
        tk.messagebox.showinfo("Error!", "There was an error in you inputs. Try again!")

    
a = tk.Label(window ,text = "What is your menstrual cycle length in days?").place(x = 100, y = 50)
b = tk.Label(window ,text = "What is your period length in days?").place(x = 100, y = 75)
c = tk.Label(window ,text = "How many sanitary products do you use per day?").place(x = 100, y = 100)
d = tk.Label(window ,text = "How many sanitary products are there per package?").place(x = 100, y = 125)
e = tk.Label(window ,text = "How much does each package cost?").place(x = 100, y = 150)

f = tk.Label(window ,text = "Enter your start date (year/month/day):").place(x = 100, y = 200)
g = tk.Label(window ,text = "Enter your end date (year/month/day):").place(x = 100, y = 225)

h = tk.Label(window ,text = "What US state do you live in (abbreviation)?").place(x = 100, y = 275)
h2 = tk.Label(window, text = "(Leave blank if you do not want to include sales tax)").place(x = 100, y = 295)
i = tk.Label(window ,text = "What is your yearly expected inflation rate (percent)?").place(x = 100, y = 325)
j = tk.Label(window, text = "(Leave blank if you do not want to include inflation)").place(x = 100, y = 345)

a1 = tk.Entry(window)
a1.place(x = 400, y = 50)
b1 = tk.Entry(window)
b1.place(x = 400, y = 75)
c1 = tk.Entry(window)
c1.place(x = 400, y = 100)
d1 = tk.Entry(window)
d1.place(x = 400, y = 125)
e1 = tk.Entry(window)
e1.place(x = 400, y = 150)

f1 = tk.Entry(window)
f1.place(x = 400, y = 200)
g1 = tk.Entry(window)
g1.place(x = 400, y = 225)

h1 = tk.Entry(window)
h1.place(x = 400, y = 275)
i1 = tk.Entry(window)
i1.place(x = 400, y = 325)

tk.Button(window, text="Submit", command = calculate).place(x = 425, y = 350)

window.mainloop()


