console.log("✅ app.js загружен и работает");

function getExpenses() {
  const food = parseFloat(document.getElementById('food-expense').value) || 0;
  const rent = parseFloat(document.getElementById('rent-expense').value) || 0;
  const clothes = parseFloat(document.getElementById('clothes-expense').value) || 0;
  return food + rent + clothes;
}

function getBalance() {
  const income = parseFloat(document.getElementById('total-income').value) || 0;
  const expenses = getExpenses();
  return income - expenses;
}

function getSavingBalance() {
  const income = parseFloat(document.getElementById('total-income').value) || 0;
  const percent = parseFloat(document.getElementById('saving-percentage').value) || 0;
  return (income * percent) / 100;
}

document.addEventListener("DOMContentLoaded", () => {
  const calcBtn = document.getElementById('calculate-btn');
  if (calcBtn) {
    calcBtn.addEventListener('click', () => {
      document.getElementById('expenses-amount').innerText = getExpenses().toFixed(2);
      document.getElementById('balance-amount').innerText = getBalance().toFixed(2);
    });
  }

  const savingBtn = document.getElementById('saving-btn');
  if (savingBtn) {
    savingBtn.addEventListener('click', () => {
      const saving = getSavingBalance();
      const balance = getBalance();
      const errorMsg = document.getElementById('saving-balance-error-msg');

      if (saving <= balance) {
        errorMsg.style.display = 'none';
        document.getElementById('saving-amount').innerText = saving.toFixed(2);
        document.getElementById('remaining-amount').innerText = (balance - saving).toFixed(2);
      } else {
        errorMsg.style.display = 'block';
        document.getElementById('saving-amount').innerText = '0';
        document.getElementById('remaining-amount').innerText = balance.toFixed(2);
      }
    });
  }
});
