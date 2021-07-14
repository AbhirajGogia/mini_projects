import React from 'react';


class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state= {timezone: props.timezone/3600, time : this.calcTime(props.timezone/3600)};


      }
    
      componentDidMount() {
        this.timerID = setInterval(
          () => this.tick(),
          1000
        );
      }
    
      componentWillUnmount() {
        clearInterval(this.timerID);
      }

      componentDidUpdate(prevProps, prevState) {
        if (prevProps.timezone !== this.props.timezone){
          let newTimezone = this.props.timezone/3600;
          this.setState({ timezone: newTimezone });  
      }
      }

      calcTime(offset) {
        let date = new Date();
        let utc = date.getTime() + (date.getTimezoneOffset() * 60000);
        var newdate = new Date(utc + (3600000*offset));
    
        // return time as a string
        return newdate;
    }
    
      tick() {
        this.setState({
          time: this.calcTime(this.state.timezone)

        });;
      }
  
    render() {
      return (
        <div>
        <h2>{this.state.time.toLocaleTimeString()}</h2>
        </div>
      );
    }
  }

  export default Clock;