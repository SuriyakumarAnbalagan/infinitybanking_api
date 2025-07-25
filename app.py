from flask import Flask, request, jsonify
from db_connection import get_db_connection
from auth import api_authenticate

app = Flask(__name__)

@app.route("/check_balance", methods=["POST"])
@api_authenticate
def check_balance():
    data = request.json
    account_number = data.get("account_number")
    pin = data.get("pin")

    if not account_number or not pin:
        return jsonify({"error": "account_number and pin are required"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT customer_name, balance, last_transaction_date 
            FROM customers 
            WHERE account_number = %s AND pin = %s
        """, (account_number, pin))

        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return jsonify({
                "status": "success",
                "customer_name": result["customer_name"],
                "balance": result["balance"],
                "last_transaction_date": str(result["last_transaction_date"])
            })
        else:
            return jsonify({"status": "error", "message": "Invalid account number or pin"}), 404

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

