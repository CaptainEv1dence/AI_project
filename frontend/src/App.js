import React, { useState } from 'react';
import './App.css';

function App() {
  const [prompt, setPrompt] = useState('');
  const [maxTokens, setMaxTokens] = useState(50);
  const [temperature, setTemperature] = useState(0.7);
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult('');

    try {
      const response = await fetch('http://localhost:8000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: prompt,
          max_new_tokens: maxTokens,
          temperature: temperature,
        }),
      });

      if (!response.ok) {
        throw new Error('API request failed');
      }

      const data = await response.json();
      setResult(data.generated);
    } catch (err) {
      setError('Ошибка при запросе к API. Проверьте, что backend запущен.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Text Generator</h1>
        <p>Powered by SmolLM2-135M-Instruct</p>
      </header>

      <main className="container">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="prompt">Введите prompt:</label>
            <textarea
              id="prompt"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Например: Write a poem about AI"
              rows="4"
              required
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="maxTokens">Max Tokens:</label>
              <input
                type="number"
                id="maxTokens"
                value={maxTokens}
                onChange={(e) => setMaxTokens(Number(e.target.value))}
                min="10"
                max="200"
              />
            </div>

            <div className="form-group">
              <label htmlFor="temperature">Temperature:</label>
              <input
                type="number"
                id="temperature"
                value={temperature}
                onChange={(e) => setTemperature(Number(e.target.value))}
                min="0.1"
                max="2.0"
                step="0.1"
              />
            </div>
          </div>

          <button type="submit" disabled={loading}>
            {loading ? 'Генерация...' : 'Сгенерировать'}
          </button>
        </form>

        {error && <div className="error">{error}</div>}

        {result && (
          <div className="result">
            <h3>Результат:</h3>
            <p>{result}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
