require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { convertAll, validateInput } = require('./utils/conversions');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.json({ ok: true, message: 'Temperature Converter API. POST /convert with { value, unit }' });
});

app.post('/convert', (req, res) => {
  const { value, unit } = req.body || {};
  const validation = validateInput(value, unit);
  if (!validation.ok) {
    return res.status(400).json({ ok: false, error: validation.error });
  }
  const result = convertAll(value, unit);
  res.json({ ok: true, input: { value, unit }, ...result });
});

// Not found handler
app.use((req, res) => {
  res.status(404).json({ ok: false, error: 'Route not found' });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ ok: false, error: 'Internal Server Error' });
});

app.listen(PORT, () => {
  console.log(`✅ API running on http://localhost:${PORT}`);
});
