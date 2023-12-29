import mysql.connector
from flask import Flask, jsonify, request

from configs.mysql import config_slave

app = Flask(__name__)


# 连接MySQL数据库
def create_conn():
    conn = mysql.connector.connect(**config_slave)
    return conn


# 查询数据的函数
def query_data(conn, param):
    cursor = conn.cursor()
    query = "SELECT * FROM test.users WHERE username = %s"
    cursor.execute(query, (param,))
    rows = cursor.fetchall()
    return rows


# REST API端点
@app.route("/api/query", methods=["GET"])
def api_query():
    param = request.args.get("username")
    if not param:
        return jsonify({"error": "miss username"}), 400

    conn = create_conn()
    data = query_data(conn, param)
    conn.close()

    if not data:
        return jsonify({"error": "未找到数据"}), 404

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
