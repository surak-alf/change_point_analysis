// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import moment from 'moment';

const App = () => {
  const [oilPrices, setOilPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [selectedEvent, setSelectedEvent] = useState(null);
  const [eventImpactData, setEventImpactData] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [error, setError] = useState(null); // For error handling

  useEffect(() => {
    fetchOilPrices();
    fetchEvents();
  }, [startDate, endDate]);

  const fetchOilPrices = async () => {
    try {
      const response = await axios.get('/api/oil_prices', {
        params: { start_date: startDate, end_date: endDate },
      });
      setOilPrices(response.data);
      setError(null); // Clear any previous errors
    } catch (error) {
      console.error("Error fetching oil prices:", error);
      setError("Error fetching oil prices. Please check your connection."); // Set error message
    }
  };

  const fetchEvents = async () => {
    try {
      const response = await axios.get('/api/events');
      setEvents(response.data);
    } catch (error) {
      console.error("Error fetching events:", error);
    }
  };

  const fetchEventImpact = async (eventName) => {
    try {
      const response = await axios.get(`/api/event_impact/${eventName}`);
      setEventImpactData(response.data);
      if (response.data.error) { // Check for error from the backend
          setError(response.data.error);
      } else {
          setError(null);
      }

    } catch (error) {
      console.error("Error fetching event impact:", error);
      setError("Error fetching event impact. Please try again.");
    }
  };

  const handleEventClick = (event) => {
    setSelectedEvent(event);
    fetchEventImpact(event.Event);
  };

  const oilPriceChartData = {
    labels: oilPrices.map(item => moment(item.Date).format('YYYY-MM-DD')),
    datasets: [
      {
        label: 'Brent Oil Price',
        data: oilPrices.map(item => item.Price),
        borderColor: 'blue',
        fill: false,
      },
    ],
  };

  const eventImpactChartData = {
    labels: eventImpactData.map(item => moment(item.Date).format('YYYY-MM-DD')),
    datasets: [
      {
        label: 'Oil Price around Event',
        data: eventImpactData.map(item => item.Price),
        borderColor: 'red',
        fill: false,
      },
    ],
  };

  return (
    <div>
      <h1>Brent Oil Price Dashboard</h1>

      {/* Date Range Filters */}
      <div>
        <label htmlFor="startDate">Start Date:</label>
        <input type="date" id="startDate" value={startDate} onChange={e => setStartDate(e.target.value)} />

        <label htmlFor="endDate">End Date:</label>
        <input type="date" id="endDate" value={endDate} onChange={e => setEndDate(e.target.value)} />
      </div>

       {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error message */}


      <Line data={oilPriceChartData} />

      <h2>Events</h2>
      <ul>
        {events.map(event => (
          <li key={event.Event} onClick={() => handleEventClick(event)}>
            {event.Event} ({moment(event.Date).format('YYYY-MM-DD')})
          </li>
        ))}
      </ul>

      {selectedEvent && (
        <div>
          <h2>Impact of {selectedEvent.Event}</h2>
          <Line data={eventImpactChartData} />
        </div>
      )}
    </div>
  );
};

export default App;