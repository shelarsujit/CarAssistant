from flask import Flask, request, jsonify
from langgraph.graph import GraphExecutor
from nodes import get_location
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

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Update the location in the AI assistant's state
    state = State(messages=[], location="", preferences={})
    get_location(state, latitude=latitude, longitude=longitude)
    
    return jsonify({"status": "Location updated successfully", "location": state['location']})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=True)
