
import os,sys
from flask import Flask, request
from flaskr.phonebook import Phonebook
from flaskr.mock_phonebook import initialize_mock

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append("..")

app = Flask(__name__)
phonebook = Phonebook(CURR_DIR_PATH + "/data/database.db")
initialize_mock(phonebook)

@app.route("/phonebook/")
def get_phonebook():
  return phonebook.get_all()

@app.route("/phonebook/name/<name_query>")
def get_by_name(name_query):
  return phonebook.get_by_name(name_query)

@app.route("/phonebook/adress/<address_query>")
def get_by_address(address_query):
  return phonebook.get_by_adress(address_query)

@app.route("/phonebook", methods=["POST", "PUT"])
def enter_record():
  json_data = request.get_json()
  phonebook.add(json_data["entry"])
  return "Added to the phonebook", 201

@app.route("/phonebook/<num_of_rows>")
def get_phonebook_rows(num_of_rows):
  return phonebook.get_rows(num_of_rows)


# loop to run the application
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)