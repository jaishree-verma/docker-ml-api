import { useState } from "react";

function App() {
  const [features, setFeatures] = useState(["", "", "", ""]);
  const [prediction, setPrediction] = useState(null);

  const handleChange = (index, value) => {
    const updated = [...features];
    updated[index] = value;
    setFeatures(updated);
  };

  const handleSubmit = async () => {
  const response = await fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ features: features.map(Number) }),
  });
  const data = await response.json();
  setPrediction(data.prediction[0]);
};

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Iris Flower Predictor 🌸</h2>
      {features.map((val, i) => (
        <input
          key={i}
          type="number"
          value={val}
          onChange={(e) => handleChange(i, e.target.value)}
          placeholder={`Feature ${i + 1}`}
          style={{ margin: "0.5rem" }}
        />
      ))}
      <br />
      <button onClick={handleSubmit}>Predict</button>
      {prediction !== null && (
        <h3>Predicted Class: {prediction}</h3>
      )}
    </div>
  );
}

export default App;
