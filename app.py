from flask import Flask, request, jsonify
import logging
import datetime

app = Flask(__name__)

# Logging setup
logging.basicConfig(level=logging.INFO)

# In-memory database
students = {}
student_id_counter = 1


# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Error: {str(e)}")
    return jsonify({"error": "Internal Server Error"}), 500


# Home route
@app.route("/", methods=["GET"])
def home():
    return "Student API is running 🚀", 200


# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# CREATE student
@app.route("/students", methods=["POST"])
def create_student():
    global student_id_counter

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    student = {
        "id": student_id_counter,
        "name": data["name"],
        "created_at": datetime.datetime.utcnow().isoformat()
    }

    students[student_id_counter] = student
    student_id_counter += 1

    logging.info(f"Student created: {student}")

    return jsonify(student), 201


# GET all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(list(students.values())), 200


# GET single student
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


# UPDATE student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    student["name"] = data["name"]
    student["updated_at"] = datetime.datetime.utcnow().isoformat()

    logging.info(f"Student updated: {student}")

    return jsonify(student), 200


# DELETE student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[student_id]

    logging.info(f"Student deleted: {student_id}")

    return jsonify({"message": "Student deleted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
