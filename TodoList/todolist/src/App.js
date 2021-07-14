import React from "react";
import TodoList from "./TodoList/todolist";

import AddTodo from "./AddTodo/addtodo";

import "./App.css";

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      todos: [],
    };
  }

  render() {
    return (
      <div>
        <h1><span id="title">Todo List</span></h1>
        <AddTodo addTodoFn={this.addTodo}></AddTodo>
        <TodoList updateTodoFn = {this.updateTodo}todos={this.state.todos}></TodoList>
      </div>
    );
  }

  componentDidMount = async () => {
    const todos = localStorage.getItem("todos");
    if (todos) {
      const savedTodos = JSON.parse(todos);
      await this.setState({ todos: savedTodos });
    } else {
      console.log("No todos");
    }
  };

  addTodo = async (todo) => {
    if (!this.state.todos.includes(todo)){
    await this.setState({ todos: [...this.state.todos, todo, 
      {text: todo, completed: false}] 
    });
    localStorage.setItem('todos', JSON.stringify(this.state.todos));
    }
  }


    updateTodo = async (todo) => {
      const newTodos = this.state.todos.map(_todo => {
        if (todo === _todo){
          return {
            text : todo.text,
            completed: !todo.completed
          }
        }
          else {
            return _todo;
          }
        });
        await this.setState({ todos : newTodos});
        localStorage.setItem('todos', JSON.stringify(this.state.todos))
    }
}

export default App;
