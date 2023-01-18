from app import app
from flask import render_template

@app.route('/')
def homepage():
    links = ['Home', 'Top 5']
    home_text = "Welcome to My homepage!"
    return render_template ('index.html', links= links, heading = home_text)

    
@app.route('/top5')
def top5Page():
    names = ['Kobe Bryant', 'Deion Sanders', 'Kam Chancellor', 'Serena Williams', 'Ed Reed']
    text = "These are my Top 5 Favorite Athletes of all time!"
    return render_template('top5.html', names = names, my_text = text)



