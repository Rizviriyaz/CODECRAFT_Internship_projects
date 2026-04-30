// utils/conversions.js
const ABS_ZERO_C = -273.15;
const ABS_ZERO_F = -459.67;
const ABS_ZERO_K = 0;

function round(n, decimals = 2) {
  const f = Math.pow(10, decimals);
  return Math.round((n + Number.EPSILON) * f) / f;
}

function toCelsius(value, unit) {
  switch (unit) {
    case 'C': return value;
    case 'F': return (value - 32) / 1.8;
    case 'K': return value - 273.15;
    default: throw new Error('Invalid unit');
  }
}

function fromCelsius(c, unit) {
  switch (unit) {
    case 'C': return c;
    case 'F': return c * 1.8 + 32;
    case 'K': return c + 273.15;
    default: throw new Error('Invalid unit');
  }
}

function convertAll(value, unit) {
  const c = toCelsius(value, unit);
  const f = fromCelsius(c, 'F');
  const k = fromCelsius(c, 'K');
  return {
    celsius: round(c),
    fahrenheit: round(f),
    kelvin: round(k),
  };
}

function validateInput(value, unit) {
  const allowed = ['C', 'F', 'K'];
  if (typeof value !== 'number' || !isFinite(value)) {
    return { ok: false, error: 'Value must be a finite number' };
  }
  if (!allowed.includes(unit)) {
    return { ok: false, error: "Unit must be one of 'C', 'F', or 'K'" };
  }
  // Absolute zero checks
  if (unit === 'C' && value < ABS_ZERO_C) {
    return { ok: false, error: `Celsius cannot be below ${ABS_ZERO_C}` };
  }
  if (unit === 'F' && value < ABS_ZERO_F) {
    return { ok: false, error: `Fahrenheit cannot be below ${ABS_ZERO_F}` };
  }
  if (unit === 'K' && value < ABS_ZERO_K) {
    return { ok: false, error: 'Kelvin cannot be below 0' };
  }
  return { ok: true };
}

module.exports = { convertAll, validateInput };
