from flask import Flask, jsonify, render_template
from config import fetch_data
import mysql.connector

app = Flask(__name__)

# @app.route("/", methods=["GET"])
# def hello_to_api():
#     return render_template('index.html')

@app.route("/user", methods=["GET"])
def user_list():
    try:
        query = "SELECT first_name, last_name,email,password,role_id,created_at,updated_at,deleted_at FROM useers"
        myresult = fetch_data(query)
        result_list = [
            {
                "first_name": row[0],
                "last_name": row[1],
                "email": str(row[2]),
                "password": str(row[3]),
                "role_id":row[4],
                "created_at": row[5],
                "updated_at": row[6],
                
            } for row in myresult
        ]
        return jsonify(result_list)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400

@app.route("/appointment", methods=["GET"])
def discarded_list():
    try:
        query = "SELECT id,start_time,end_time,appointment_status FROM practice"
        myresult = fetch_data(query)
        result_list = [
            {
                "id":
                row[0],
                "start_time": str(row[1]),
                "end_time": str(row[2]),
                "appointment_status": str(row[3])
                
            } for row in myresult
        ]
        return jsonify(result_list)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# @app.route("/user", methods=["GET"])
# def user_list():
#     try:
#         query = "SELECT first_name, last_name,email,password,role_id,created_at,updated_at,deleted_at FROM useers"
#         myresult = fetch_data(query)
#         result_list = [
#             {
#                 "first_name": row[0],
#                 "last_name": row[1],
#                 "email": str(row[2]),
#                 "password": str(row[3]),
#                 "role_id":row[4],
#                 "created_at": row[5],
#                 "updated_at": row[6],
                
#             } for row in myresult
#         ]
#         return jsonify(result_list)
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 400

    

# @app.route("/app", methods=["GET"])
# def time_slots():
#     try:
#         query = "SELECT time_slot FROM timeslots"
#         myresult = fetch_data(query)
#         result_list = [{"timeslots": row[0]} for row in myresult]
#         return jsonify(result_list)
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 500

# @app.route("/slots_completed_field", methods=["POST", "GET"])
# def slots_completed():
#     try:
#         query = "SELECT timeslot FROM timeslots"
#         myresult = fetch_data(query)
#         all_slots_booked = all(slot[0] == 'booked' for slot in myresult)
#         message = {
#             "status": "success",
#             "message": "ALL_SLOTS_BOOKED" if all_slots_booked else "NOT_ALL_SLOTS_BOOKED"
#         }
#         return jsonify(message)
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 500

if __name__ == "__main__":
    app.run(debug=True)