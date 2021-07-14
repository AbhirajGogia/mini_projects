import React from "react";
import "./style.css";

class AddTodo extends React.Component {
  constructor() {
    super();
    this.state = {
      todo: "",
    };
  }
  render() {
    return (
      <div className="addTodoContainer" id="footer">
        <form onSubmit={(e) => this.submitTodo(e)}>
          <div>
            <input
              placeholder="Todo item"
              id="addTodoInput"
              onChange={(e) => this.updateInput(e)}
              type="text"
            ></input>
          </div>
          <div>
            <button className="btn" type="submit">
              Add
            </button>
          </div>
        </form>
        <form onSubmit= {(e) => this.resetTodos(e)}>
        <div>
            <button className="btn" type="submit">
              Clear All Todos
            </button>
          </div>
        </form>
      </div>
    );
  }

  updateInput = (e) => {
    this.setState({ todo: e.target.value });
  };
  submitTodo = (e) => {
    e.preventDefault();
    this.props.addTodoFn(this.state.todo);
    document.getElementById("addTodoInput").value = "";
  };

  resetTodos = (e) => {
    localStorage.clear();
    this.setState({todo : ''})
  }
}
export default AddTodo;
