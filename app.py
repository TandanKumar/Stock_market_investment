from flask import Flask
from stock_market.logger import logging
logging.info("start of the program")

app= Flask(__name__)

@app.route ("/",methods=['GET','POST'])
def index():
    logging.info("We are testing the project")
    return"CI/CD  for new with sdasdsadasd  logger testing pipeline is happening"

if __name__== "__main__":
    app.run(debug=True) 
    
