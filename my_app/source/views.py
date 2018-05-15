from flask import Flask, render_template, flash, request, Blueprint, redirect, url_for, session, abort
app = Flask(__name__)


from my_app.source.models import cursor
from my_app.source.mode import cursor1
from my_app.source.modelo import cursor2

my_view = Blueprint('my_view', __name__)

#home page handler
@my_view.route("/")
@my_view.route("/home")
def home():
    if not session.get('logon'):
        return render_template('login.html')
    else:
        return render_template('index.html')


#handler login
@my_view.route('/login', methods=['POST'])
def admin_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['logon'] = True
    else:
        flash('Incorrect!')
    return home()

#logout handler
@my_view.route("/logout")
def logout():
    session['logon'] = False
    return home()
    
#invoice handler
@my_view.route("/changelogs")
def invoice():
    command = """SELECT {a}.id, {a}.version, {a}.detail, {a}.date, {b}.version
                      From {a} join {b} ON {a}.id = {b}.id
        """.format(a="changelogs", b='cool')
    cursor1.execute(command)
    kim = cursor1.fetchall()      
    return render_template('changelogs.html', my_chin = kim)


#payment
@my_view.route("/ticket")
def tck():
    command = """SELECT {a}.id, {a}.name, {a}.value, {b}.name
                      FROM {a} join {b} ON {a}.category_id = {b}.id
        """.format(a="tics", b='category')
    cursor.execute(command)
    astro_data = cursor.fetchall()  


    return render_template('ticket.html', my_list=astro_data)
    
#payment
@my_view.route("/users")
def users():
    command = """SELECT {a}.id, {a}.staff, {a}.position,  {a}.email, {b}.staff
                      FROM {a} join {b} ON {a}.id = {b}.id
        """.format(a="altimit", b='staff')
    cursor2.execute(command)
    staff_data = cursor2.fetchall()  


    return render_template('users.html', my_staff=staff_data)
    




#order
@my_view.route("/ticket")
def orders():
    return render_template('ticket.html')


