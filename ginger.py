
# -*-coding:utf-8-*-
from app.app import create_app

__author__ = 'ZeroLoo'

app=create_app()

@app.route("/index/")
def get_user():
    return "e21321312"

if __name__=='__main__':
    app.run(debug=True)