document.getElementById("generateBtn").addEventListener("click", async () => {
    const topic = document.getElementById("topic").value;
    const wordCount = document.getElementById("wordCount").value;
    document.getElementById("joke").textContent = "Generating... Here's a joke while you wait!";

    try {
        const response = await fetch("/generate-recipe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ topic, wordCount }),
        });

        const data = await response.json();
        document.getElementById("joke").textContent = data.joke;
        document.getElementById("output").innerHTML = `<h2>Generated Recipe</h2><p>${data.recipe}</p>`;
    } catch (error) {
        document.getElementById("output").innerHTML = "<p style='color: red;'>Error generating recipe. Try again!</p>";
    }
});
