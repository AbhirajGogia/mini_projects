import React from 'react'
import './style.css';

class TodoItem extends React.Component {

    render() {

        const {todo} = this.props
        return(<div className = "todoSlot"><span className = {"todoItem" + (todo.completed ? ' completed' : '') + (todo.text ? ' todoExists' : '') } onClick={this.toggleTodo}>{todo.text}</span></div>)
    }

    toggleTodo = () => {
        this.props.updateTodoFn(this.props.todo)

    }

}



export default TodoItem