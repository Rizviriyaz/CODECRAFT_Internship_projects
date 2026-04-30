import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

// Store game state in memory (per server run)
let targetNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

app.post("/guess", (req, res) => {
  const { guess } = req.body;
  attempts++;

  if (!guess || typeof guess !== "number") {
    return res.status(400).json({ ok: false, message: "Invalid input" });
  }

  if (guess < targetNumber) {
    return res.json({ ok: true, result: "too low", attempts });
  } else if (guess > targetNumber) {
    return res.json({ ok: true, result: "too high", attempts });
  } else {
    const finalAttempts = attempts;
    // Reset game for replay
    targetNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;
    return res.json({ ok: true, result: "correct", attempts: finalAttempts });
  }
});

app.listen(3000, () => console.log("🎮 Guessing Game API running on http://localhost:3000"));
