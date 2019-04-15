from flask import render_template, request, redirect, url_for, abort, session
from server import app, system
from datetime import datetime

'''
Website Structure:
- Home page '/'
- #Customer '/customer'
    - Menu pages '/customer/menu' 
        - Mains '/customer/mains'
            - Creation '/customer/mains/creation'
        - Sides '/customer/sides'
        - Drinks /customer/drinks'
    - Review order '/customer/review/<order_id>'
    - Order tracking  '/customer/order/<order_id>'
- #Staff '/staff'
    - Login '/staff/login'
    - Logout '/staff/logout'
    - Order '/staff/order'
    - Inventory '/staff/inventory'
'''


'''
page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


@app.route('/', methods=["GET", "POST"])
def home_page():
    print(session)
    if request.method == 'POST': 
        if request.form["button"] == "make_new_order":
            order_id = system.make_order()
            session['order_ID'] = order_id
            return redirect('/customer/menu/Mains')
        elif request.form["button"] == "continue_order":
            return redirect('/customer/menu/Mains')
        elif request.form["button"] == "search_order":
            return redirect(url_for('search_order', order_id=request.form['order_id']))
        elif request.form["button"] == "staff":
            return redirect(url_for('staff_homepage'))

    return render_template('home_page.html')


'''
Customer pages:
'''
@app.route('/customer/menu/<menu_name>', methods=["GET", "POST"])
def display_menu(menu_name):
    menu = system.get_menu(menu_name)
    if not menu:
        return redirect(url_for('page_not_found'))

    if request.method == 'POST':
        #item = menu.get_item(request.form["button"])
        item = system.get_item(request.form["button"])
        print(item)
        system.add_items_in_orders(session['order_ID'], item)
    
    return render_template('menus.html', menu_name=menu_name, menu=menu.display(), inventory=system.inventory)
    

@app.route('/customer/review', methods=["GET", "POST"])
def review_order():
    if 'order_ID' not in session:
        return "Sorry, we cannot find your order."

    order = system.get_order(session['order_ID'])
    if request.method == 'POST':
        if request.form["button"] == "checkout":
            order_id = session['order_ID']
            system.checkout(order_id)
            session.pop('order_ID')
            return render_template("order_result.html", order_id=order_id) 
        else:
            system.del_items_in_orders(order.order_id, request.form["button"])
    
    return render_template('review_order.html', order=order)


@app.route('/customer/order/<order_id>')
def search_order(order_id):
    return render_template('search_order_result.html', order=system.get_order(int(order_id)))


'''
Staff pages:
'''
@app.route('/staff')
def staff_homepage():
    if system.is_authenticated:
        return redirect(url_for('staff_order'))
    else:
        return redirect(url_for('staff_login'))


@app.route('/staff/login', methods=["GET", "POST"])
def staff_login():

    if request.method == 'POST':
        if request.form['button'] == "login":
            if system.staff_login(request.form['username'], request.form['password']):
                return redirect(url_for('staff_order'))
            else:
                return render_template('staff_login.html', username=request.form['username'], error=True)
        
        elif request.form['button'] == "cancel":
            return redirect(url_for('home_page')) 
    
    return render_template('staff_login.html', username=None, error=None)


@app.route('/staff/logout')
def staff_logout():
    system.staff_logout()
    return redirect(url_for('home_page'))


@app.route('/staff/order', methods=["GET", "POST"])
def staff_order():
    if not system.is_authenticated:
        return redirect(url_for('staff_login')) 

    if request.method == 'POST':
        order_id = int(request.form['button'])
        system.update_order(order_id)

    return render_template('staff_order.html', system=system)

@app.route('/staff/inventory', methods=["GET", "POST"])
def staff_inventory():
    if not system.is_authenticated:
        return redirect(url_for('staff_login'))

    return render_template('staff_inventory.html', system=system)

'''
---- Supplied codes ----:
'''


'''
Search for Cars
'''
@app.route('/car', methods=["GET", "POST"])
def cars():

    if request.method == 'POST':
        make  = request.form.get('make')
        model = request.form.get('model')

        if make == '':
            make = None

        if model == '':
            model = None

        cars = system.search_car(make, model)
        return render_template('cars.html', cars = cars)
    
    return render_template('cars.html', cars = system.cars)


'''
Display car details for the car with given rego
'''
@app.route('/cars/<rego>')
def car(rego):
    car = system.get_car(rego)

    if not car:
        abort(404)

    return render_template('car_details.html', car=car)


'''
Make a booking for a car with given rego
'''
#from src.forms import BookingForm
@app.route('/cars/book/<rego>', methods=["GET", "POST"])
def book(rego):
    car = system.get_car(rego)

    if not car:
        abort(404)
    if request.method == 'POST':
        form = BookingForm(request.form)
        # 1. If form is not valid, then display appropriate error messages
        if not form.is_valid:
            errors = {field.name: form.get_error(field.name) for field in form._fields}
            errors["period"] = form.get_error("period")
            return render_template('booking_form.html', car=car,errors=errors,checked=False,form=form) 
            # 2. If the user has pressed the 'check' button, then display the fee
        
        if request.form['button'] == "check_booking":
            fee = system.check_fee(car, form.start_date, form.end_date)
            return render_template('booking_form.html', car=car,errors={},checked=True,fee=fee,form=form)
        # 3. Otherwise, if the user has pressed the 'confirm' button, then 
        #   make the booking and display the confirmation page
        elif request.form['button'] == "confirm":
            customer = Customer(form.customer_name, form.customer_licence)
            booking = system.make_booking(customer, car, form.start_date, form.end_date, form.start_location, form.end_location)
            return render_template('booking_confirm.html', booking=booking)
        elif request.form['button'] == "cancel":
            pass
    return render_template('booking_form.html', car=car,errors={},checked=False,form=None)

'''
Display list of all bookings for the car with given 'rego'
'''
@app.route('/cars/bookings/<rego>')
def car_bookings(rego):
    return render_template('bookings.html', bookings=system.get_bookings_by_car_rego(rego))