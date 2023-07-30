import psutil  #library for monitoring system util
from flask import Flask, render_template  # flask = workframe

app = Flask(__name__) # 

@app.route("/")
# home path = /   user comes in = the home path of the app run

def index():
    cpu_percent = psutil.cpu_percent()   #holds the value of the cpu usage
    mem_percent = psutil.virtual_memory().percent #holds the value of the memory 
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "High CPU/Mem Utilziation. Need to scale up"
    return render_template ("index.html" , cpu_percent=cpu_percent , mem_percent=mem_percent, message=Message)

if __name__ == '__main__':                
    app.run(debug=True, host='0.0.0.0')                #run the app , host of application 0000-local

