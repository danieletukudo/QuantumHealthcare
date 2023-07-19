from flask import Flask, render_template, request
import mysql.connector
import smtplib
app = Flask(__name__)
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='quantum'
# )
# # Configure SMTP email settings
# smtp_host = 'smtp.gmail.com'
# smtp_port = 587
# smtp_username = 'igatajohn15@gmail.com'
# smtp_password = 'trailblazer1'
@app.route('/')
def home():
    image_urls = [
        '/static/1.jpg',
        '/static/2.jpg',
        '/static/3.jpg',
        '/static/device5.jpg'
    ]
    return render_template('home.html', image_urls=image_urls)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product')
def product():
    return render_template('product.html')


# @app.route('/place_order', methods=['GET', 'POST'])
# def place_order():
#     if request.method == 'POST':
#         # Retrieve form data
#         name = request.form['name']
#         email = request.form['email']
#         address = request.form['address']
#         phone = request.form['phone']

#         # Save order details to the database
#         cursor = db.cursor()
#         query = "INSERT INTO orders (name, email, address, phone) VALUES (%s, %s, %s, %s)"
#         values = (name, email, address, phone)
#         cursor.execute(query, values)
#         db.commit()

#         # Send confirmation email
#         sender_email = 'your_email@example.com'
#         receiver_email = email
#         message = f"Dear {name},\n\nThank you for placing your order with us.\n\nWe will process your order and provide further updates soon.\n\nBest regards,\nYour Company Name"
#         smtp_server = smtplib.SMTP(smtp_host, smtp_port)
#         smtp_server.starttls()
#         smtp_server.login(smtp_username, smtp_password)
#         smtp_server.sendmail(sender_email, receiver_email, message)
#         smtp_server.quit()

#         # Render the confirmation page
#         return render_template('confirmation.html', name=name)

#     return render_template('order.html')
@app.route('/order',methods=['GET','POST'])
def order():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        # phone=request.form['phone']
        address=request.form['address']
        return render_template('confirmation.html')
    return render_template('order.html')
@app.route('/payment')
def payment():
    return render_template('payment.html')
if __name__=="__main__":
    app.run(debug=True)