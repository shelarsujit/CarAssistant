from flask import Flask, request, jsonify
from langgraph.graph import GraphExecutor
from graph import graph
from state import State

app = Flask(__name__)

executor = GraphExecutor(graph)

@app.route('/assist', methods=['POST'])
def assist():
    initial_state = State(messages=[], location="", preferences={})
    user_input = request.json.get("query")
    initial_state['messages'].append({"role": "user", "content": user_input})
    final_state = executor.run(initial_state)
    response = final_state['messages'][-1]['content']
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)
