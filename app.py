import joblib
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os
import inference
#Creating an instance for the flask app
app = Flask(__name__)
Bootstrap(app) #pass app into the bootstrap class to use Boostrap functions

#route when we recieve a GET or POST request from the index page
@app.route('/', methods = ['POST', 'GET'])

def index():
    if request.method == "GET":
        #render the index page
        return render_template('index.html')
    
    #when the URL has been submitted
    if request.method == "POST":
        
        #extract the URL
        text = request.form['url']  
        
        #check if the URL belongs to India subreddit
        if 'india' not in text:
            result = {
            'flair': "does not belong to the subreddit 'India'",
            }
            return render_template('show.html', result=result)
        
    if text != ' ': #check if the click was valid
        
        #get the predicted class name from the inference module function
        flair_type = inference.get_flair(url=text)
        flair_type = list(flair_type)[0]
        print('The following post belongs to: {}'.format(flair_type))  #display the result
        
        #result to be displayed 
        result ={
        'flair': flair_type,
        }
    return render_template('show.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)    
