# Temperature Converter API (Express)

## Setup
1) Install Node.js (LTS).
2) In this `backend` folder, run:
```bash
npm install
npm run dev   # or: npm start
```
API runs on `http://localhost:3000`.

## Endpoints
- `GET /` – health/info
- `POST /convert` – body: `{ "value": 25, "unit": "C" }`

### Example `curl`
```bash
curl -X POST http://localhost:3000/convert \
  -H "Content-Type: application/json" \
  -d "{\"value\": 25, \"unit\": \"C\"}"
```
