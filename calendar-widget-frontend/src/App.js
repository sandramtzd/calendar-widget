// src/App.js
import React, { useEffect, useState } from "react";

function App() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://calendar-widget-backend.onrender.com/events") // Adjust path if needed
      .then((res) => {
        if (!res.ok) throw new Error("Network response not ok");
        return res.json();
      })
      .then((data) => {
        setEvents(data.events || data); // adapt if your data shape is different
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading events...</p>;
  if (error) return <p>Error: {error}</p>;
  if (events.length === 0) return <p>No upcoming events found.</p>;

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", fontFamily: "Arial, sans-serif" }}>
      <h2>My Calendar Events</h2>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {events.map((event) => (
          <li key={event.id} style={{ marginBottom: 16, borderBottom: "1px solid #ddd", paddingBottom: 8 }}>
            <strong>{event.summary || event.title}</strong>
            <br />
            <small>
              {new Date(event.start.dateTime || event.start.date).toLocaleString()} -{" "}
              {new Date(event.end.dateTime || event.end.date).toLocaleString()}
            </small>
            <p>{event.description || ""}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;