// PocketSmart AI Logic
let expenses = [];
let balance = 0;

function addExpense() {
  const amount = document.getElementById('amount').value;
  const category = document.getElementById('category').value;
  const desc = document.getElementById('desc').value;

  if(!amount) { alert("Amount podu di Muthu!"); return; }

  const expense = { amount: parseFloat(amount), category, desc, date: new Date().toLocaleDateString() };
  expenses.push(expense);
  balance -= expense.amount;
  
  updateUI();
  getAIAdvice(expense);
  
  // Clear
  document.getElementById('amount').value = '';
  document.getElementById('desc').value = '';
}

function updateUI() {
  document.getElementById('balance').innerText = `₹${balance.toFixed(2)}`;
  
  let listHTML = '';
  expenses.forEach((e, i) => {
    listHTML += `<li><span>${e.category}: ${e.desc}</span><span>₹${e.amount}</span></li>`;
  });
  document.getElementById('expenseList').innerHTML = listHTML;
}

async function getAIAdvice(expense) {
  const aiBox = document.getElementById('aiBox');
  aiBox.innerHTML = "✨ AI Yosikuthu di Muthu...";

  // Gemini AI API call logic (Flask backend ku anupum)
  try {
    const res = await fetch('/get-advice', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ expense, totalSpent: expenses.reduce((a,b)=>a+b.amount,0) })
    });
    const data = await res.json();
    aiBox.innerHTML = `🤖 <b>PocketSmart:</b> ${data.advice}`;
  } catch {
    aiBox.innerHTML = `🤖 <b>PocketSmart:</b> Ayyo ${expense.category} la ₹${expense.amount} selavu pannitta! Konjam control pannu di Muthu, savings mukkiyam!`;
  }
}