from flask import Flask, request, render_template
app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'

db = SQLAlchemy(app)

import pandas as pd
import numpy as np
#import tensorflow as tf
#from tensorflow import keras

class User(db.Model):
   id = db.Column(db.Integer, primary_key =True)
   username = db.Column(db.String(100), nullable = False)



def pred():
    df = pd.read_csv('graph/BRITANNIA.csv')
    #print(df)

    data=[]
    for row in df:
        data.append(df[row])
        #print(row)

    df = df.fillna(0) #change Nan values to 0


    trades = df['Trades'].tolist() #store the Trades values in a list

    trades = trades[2850:] #remove 0 values
    #print(trades)

    #plt.plot(trades)
    #plt.ylabel('price')
    #plt.show()



    train_data = trades[:2000]
    test_data = trades[2000:]
    #print(train_data)
    #print(test_data)

    maximum = df['Trades'].max()

    td = np.array(trades)  #normalize the data by dividing the values with the maximum value
    td = td/maximum
    #print(td)


    list_inp=[]
    list_out=[]
    for i in range(5,len(td)):
        list_inp.append(td[i-5:i])
        list_out.append(td[i])

    inp_test = np.array(list_inp[2000:])
    inp_test = inp_test.reshape(inp_test.shape[0],inp_test.shape[1],1)
    #print(inp_test.shape)
    out_test = np.array(list_out[2000:])
    #print(out_test.shape)
    
    #model = keras.models.load_model('chat_model.h5')
    
    ans=[]
    for i in inp_test[:10]:
        a = i
        a = a.reshape(1,a.shape[0],a.shape[1])
        #y = model.predict(a)
        #ans.append(y[0][0]*maximum)
        ans.append(i)
    return ans[0]
	
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/fight')
def cre():
    return "figh"

@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['Search']
        ans = pred()
        
        user1 = User(username = user)
        db.session.add(user1)
        db.session.commit()
        
        return "hello " +user+"\n"+str(ans)
    else:
        return "yo kun"
    return 'hel'
