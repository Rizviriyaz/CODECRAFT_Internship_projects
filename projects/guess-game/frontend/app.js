const API_BASE = "http://localhost:3000";

async function makeGuess() {
  const guess = parseInt(document.getElementById("guessInput").value);
  if (!guess) {
    alert("Please enter a number!");
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/guess`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ guess })
    });

    const data = await res.json();

    if (data.ok) {
      document.getElementById("result").textContent = 
        data.result === "correct" 
          ? `🎉 Correct! You won in ${data.attempts} attempts.` 
          : `Your guess is ${data.result}.`;

      if (data.result === "correct") {
        document.getElementById("attempts").textContent = "New game started!";
      } else {
        document.getElementById("attempts").textContent = `Attempts: ${data.attempts}`;
      }
    } else {
      alert(data.message);
    }
  } catch (err) {
    console.error(err);
    alert("Error connecting to server.");
  }
}
