from flask import Flask, render_template, request,redirect,url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dhinesh@2778',
    'database': 'dada'
}

@app.route('/app')
def new():
    return "welcome to flask"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addata', methods=['POST'])
def index1():
    if request.method == 'POST':
        name = request.form.get('name')
        
        email = request.form.get('email')
 
        # Establishing a connection to MySQL database
        con = mysql.connector.connect(**mysql_config)
        cur = con.cursor()

        # Creating the table if not exists
        cur.execute('''
            CREATE TABLE IF NOT EXISTS mydb1 (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                
                email VARCHAR(255)
            )
        ''')

        # Inserting data into the MySQL database
        cur.execute("INSERT INTO mydb1(name,  email) VALUES (%s, %s)", (name,  email))
        con.commit()
        con.close()

        msg = "Data created successfully"

        return render_template("success.html", msg=msg)

@app.route("/view")
def view():
    # Establishing a connection to MySQL database
    con = mysql.connector.connect(**mysql_config)
    cur = con.cursor(dictionary=True)

    # Fetching data from MySQL database
    cur.execute("SELECT * FROM mydb1")
    rows = cur.fetchall()

    con.close()
    return render_template("view.html", rows=rows)

@app.route('/del')
def index2():
    return render_template("delete.html")

@app.route('/deleterecord', methods=['POST','DELETE'])
def delete():
    if request.method == 'POST' or request.method == 'DELETE':
        name = request.form.get('name')

        # Establishing a connection to MySQL database
        con = mysql.connector.connect(**mysql_config)
        cur = con.cursor() #to start the further codes

        # Deleting record from MySQL database
        cur.execute('DELETE FROM mydb1 WHERE name=%s', (name,))
        con.commit() #to save 
        con.close() #to close

        # dhin = "Delete successful"
        # return render_template("delete.html",dhin=dhin)
        return redirect(url_for("view"))
        

if __name__ == "__main__":
    app.run(debug=True)
