from flask import Flask, redirect, url_for, request, render_template
from Slprj import *

app = Flask(__name__, template_folder="templates")


@app.route('/TabletTrack', methods=['POST', 'GET'])
def tabletTrack():
    if (request.method == "POST"):
        rn = request.form['rn']
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']
        date = str(year) + "-" + str(month) + "-" + str(day)
        tablet = tab(rn, date)
        tablet.InsertingIntoTabletabTaken(rn, date)
        # return("HELLOOOOOOOOOO")
        return (redirect(url_for('success')))
    else:
        return ("Unsuccessful")


@app.route('/EnteringName', methods=['POST', 'GET'])
def EnteringName():
    if (request.method == "POST"):
        print("Reached Enter_name")
        fname = request.form['fname']
        print("Got fname")
        rn = request.form['rn']
        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        # return (redirect(url_for('EnterDetails', name=(fname, rn, age, gender, height, weight))))
        nS = student(rn, age, weight, height, gender, fname)
        nS.InsertingIntoTablenewStud(rn, fname, age, gender, height, weight)
        # return (redirect(url_for("Index.html")))
        return (redirect(url_for('success')))
    else:
        return ("UNSUCESSFUL")
    # return (redirect(url_for('EnterDetails', name=(fname, rn, age, gender, height, weight))))
    # else:
    #  return ("UNSUCCESSFUL!!!!")


@app.route('/success')
def success():
    return render_template('Successful.html')


if __name__ == '__main__':
    print("Reached the py file")
    app.run(debug=True)
