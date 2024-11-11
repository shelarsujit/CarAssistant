from langgraph.graph import GraphExecutor
from graph import graph
from state import State

def main():
    initial_state = State(messages=[], location="", preferences={})
    executor = GraphExecutor(graph)
    
    while True:
        user_input = input("How can I assist you today? ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        initial_state['messages'].append({"role": "user", "content": user_input})
        final_state = executor.run(initial_state)
        response = final_state['messages'][-1]['content']
        print(response)

if __name__ == "__main__":
    main()
