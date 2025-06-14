document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('myChart');

    const labels = JSON.parse(canvas.dataset.labels);
    const dataIncome = JSON.parse(canvas.dataset.income);
    const dataExpenses = JSON.parse(canvas.dataset.expenses);

    const ctx = canvas.getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Income',
                    data: dataIncome,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Expenses',
                    data: dataExpenses,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
