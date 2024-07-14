document.getElementById('calcForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ num1: num1, num2: num2 })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sum').textContent = data.sum;
        document.getElementById('multiplication').textContent = data.multiplication;
    });
});
