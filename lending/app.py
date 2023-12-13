from flask import Flask, render_template, request, url_for, flash,session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def lending():
    how_many_years = None
    number_of_months = 0  # Initialize the variable with a default value
    other_charges = 0  # Initialize the variable with a default value
    
    monthly = 0
    anual = 0
    total_charger = 0
    total_minus = 0
    interest =  0.00805
    rounded_anual = 0 
    monthly_payment = 0
    annual_interest_rate = 9.66
    sweary = 0
    round_round = 0 
    result = []
    monthly_payment_rounded = 0
    loan = 0
    net_proc = 0
    outstanding_balance = 0
    interest_rate = 0.00805
    monthly_interest = []
    outstanding_balancesss = 0
    principal = 0
    if request.method == 'POST':
        how_many_years = int(request.form['how_many_years'])
        principal = float(request.form['principal'])
        loan =principal
        number_of_months = how_many_years * 12  # Calculate the number of months
        other_charges = principal * 0.06
      
        
        anual = principal * 0.0966
        rounded_anual  = round(anual, 2) 
        total_charger = other_charges + monthly +anual
        total_minus = principal - total_charger / number_of_months
        interest  =principal * interest_rate
        monthly_interest_rate = annual_interest_rate / 100 / 12

        # Calculate monthly payment using the amortization formula
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_months) / \
                      ((1 + monthly_interest_rate) ** number_of_months - 1)
        
        monthly_payment_rounded = round(monthly_payment, 2) 
# Calculate interest amount
        annual_interest_rate = principal * (annual_interest_rate / 100)
        
        sweary = monthly_payment_rounded - interest
        round_round  = round(sweary, 2) 
        net_pro = principal - other_charges
        net_proc  = round(net_pro, 2) 
        
        for i in range(1, number_of_months + 1):
            result.append(loan)
            
            # Assuming you want the interest for the current month
            current_monthly_interest = float("{:.2f}".format(result[-1] * interest_rate))
            monthly_interest.append(current_monthly_interest)

            loan -= monthly_payment - current_monthly_interest
            outstanding_balance = [round(value, 2) for value in result]

            # Calculate the new outstanding balance after deducting the interest
            sweary = [monthly_payment_rounded - interest for interest in monthly_interest]
            outstanding_balancesss = [round(value - s, 2) for value, s in zip(outstanding_balance, sweary)]

    return render_template('index.html',outstanding_balancesss=outstanding_balancesss,sweary=sweary,interest=interest,monthly_interest=monthly_interest,outstanding_balance=outstanding_balance,net_proc=net_proc,principal=principal,round_round=round_round, how_many_years=how_many_years, number_of_months=number_of_months, other_charges=other_charges,interest_rate=interest_rate,rounded_anual=rounded_anual, total_minus=total_minus,annual_interest_rate=annual_interest_rate, monthly_payment=monthly_payment,monthly_payment_rounded=monthly_payment_rounded,loan = loan)
 
 
 
 
 
 
 
 
 
 
 
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)