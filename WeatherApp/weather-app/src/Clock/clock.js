import React from 'react';


class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state= {timezone: props.timezone/3600, time : this.calcTime(props.timezone/3600)};
        
        // console.log(this.state.time.getTime()/1000, this.state.time.getTimezoneOffset()*60, this.state.timezone)
        // this.state.seconds = (this.state.time.getTime()/1000 - this.state.time.getTimezoneOffset()*60 + this.state.timezone);
        // this.state.date = new Date(this.state.seconds).toISOString().substr(11, 8);
        // console.log(this.state.date);

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
          // seconds: (this.state.time.getTime()/1000 - this.state.time.getTimezoneOffset()*3600 + this.state.timezone),
          // date: new Date(this.state.seconds).toISOString().substr(11, 8)

        });;
        // let shift = this.state.time.getMilliseconds();
        // this.state.time.setMilliseconds(shift + this.state.timezone*1000)
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