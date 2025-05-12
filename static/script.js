document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("expense-form");
    const list = document.getElementById("expense-list");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const amount = document.getElementById("amount").value;
        const category = document.getElementById("category").value;
        const description = document.getElementById("description").value;

        const response = await fetch("/add", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ amount, category, description })
        });

        const result = await response.json();
        alert(result.message);
        form.reset();
        loadExpenses();
    });

    async function loadExpenses() {
        const response = await fetch("/expenses");
        const expenses = await response.json();

        list.innerHTML = "";
        expenses.forEach(exp => {
            const item = document.createElement("li");
            item.textContent = `${exp.date} - ${exp.amount}€ - ${exp.category} : ${exp.description}`;
            list.appendChild(item);
        });
    }

    loadExpenses();
});
