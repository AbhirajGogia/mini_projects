import './index.css';
import React, { useState } from 'react';
import Clock from './Clock/clock.js'

const api = {
  key: 'bb485acca8ffaa50f02067f9430c5810',
  base: 'https://api.openweathermap.org/data/2.5/'
}

function App() {

  const [query, setQuery] = useState('');
  const [weather, setWeather] = useState({});


  const search = e => {
    if (e.key === "Enter") {
      fetch(`${api.base}weather?q=${query}&units=metric&APPID=${api.key}`)
        .then(res => res.json())
        .then(result => {
          setWeather(result);
          setQuery('')

        });
    }
  }


  const dateBuilder = (d) => {
    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`

  }




  return (
    <div className={(typeof weather.main != "undefined") ? (`app ${weather.weather[0].main.toString().toLowerCase()}`) : "app"}>
      <main>
        <div className="search-box">
          <input
            type="text"
            className="search-bar"
            placeholder="search"
            onChange={e => setQuery(e.target.value)}
            value={query}
            onKeyPress={search} />

        </div>


        {(typeof weather.main != 'undefined') ? (

          <div>
            <div className="location-box">
              <div className="location">{weather.name}, {weather.sys.country}</div>
              <div className="date">{dateBuilder(new Date())}</div>
            </div>
            <div className="weather-box">
              <div className="temp">
                {Math.round(weather.main.temp)}˚C
              </div>
              <div className="weather">
                {weather.weather[0].main}
              </div>
            </div>
          </div>
        ) : ('')}

        {(typeof weather.timezone != 'undefined') ? (
        <div className ="clock">

          <Clock timezone={weather.timezone}/>
          

        </div>
        ) : (
          <div className="title-box">
          <div className="title">Weather</div>
          <div className="title">&</div>
          <div className="title">Local Time</div>
          <br></br>
          <div className="smaller-title">By Raj Gogia</div>
          </div>
        
        
          )}

      </main>
    </div >
  );
}

export default App;



