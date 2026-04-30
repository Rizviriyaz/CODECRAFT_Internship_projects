// Frontend logic
const API_BASE = 'http://localhost:3000'; // Change if backend runs elsewhere

const form = document.getElementById('convert-form');
const out = document.getElementById('output');
const errBox = document.getElementById('error');
const cEl = document.getElementById('celsius');
const fEl = document.getElementById('fahrenheit');
const kEl = document.getElementById('kelvin');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  errBox.classList.add('hidden');
  out.classList.add('hidden');

  const value = parseFloat(document.getElementById('value').value);
  const unit = document.getElementById('unit').value;

  try {
    const res = await fetch(`${API_BASE}/convert`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ value, unit })
    });
    const data = await res.json();

    if (!res.ok || !data.ok) {
      throw new Error(data.error || 'Something went wrong');
    }

    cEl.textContent = `${data.celsius} °C`;
    fEl.textContent = `${data.fahrenheit} °F`;
    kEl.textContent = `${data.kelvin} K`;

    out.classList.remove('hidden');
  } catch (err) {
    errBox.textContent = err.message;
    errBox.classList.remove('hidden');
  }
});
