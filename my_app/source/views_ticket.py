from flask import render_template, request, redirect, url_for, flash

from my_app.source.models import cursor, conn


#-------------------- Tickets Handler --------------------
def tickets():   
    command = """SELECT {a}.id, {a}.issue, {b}.issue
                      FROM {a} join {b} ON {a}.risk_id = {b}.id
        """.format(a="ticket", b='risks')
    cursor.execute(command)
    ticket_data = cursor.fetchall()  


    return render_template('ticket.html', my_list=ticket_data)
    
