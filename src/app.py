from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)

    if 'label' in request_body and 'done' in request_body:
        todos.append(request_body)
        return jsonify(todos)
    else:
        return 'Error: The request body must contain "label" and "done" keys.', 400

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    if position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return 'Error: Task not found at given position.', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
