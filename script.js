function drawGraph() {
  const functionSelect = document.getElementById("function").value;
  const xMin = parseFloat(document.getElementById("xMin").value);
  const xMax = parseFloat(document.getElementById("xMax").value);

  // Membuat data untuk grafik
  const data = {
    labels: [],
    datasets: [
      {
        label: getFunctionLabel(functionSelect),
        data: [],
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
        fill: false,
      },
    ],
  };

  for (let x = xMin; x <= xMax; x += (xMax - xMin) / 100) {
    data.labels.push(x.toFixed(2));
    data.datasets[0].data.push(calculateY(functionSelect, x));
  }

  const ctx = document.getElementById("chart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: data,
    options: {
      responsive: true,
      scales: {
        x: {
          beginAtZero: true,
        },
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

function getFunctionLabel(func) {
  switch (func) {
    case "sin":
      return "Sinus (sin(x))";
    case "cos":
      return "Kosinus (cos(x))";
    case "parabola":
      return "Parabola (x^2)";
    default:
      return "Fungsi Tidak Diketahui";
  }
}

function calculateY(func, x) {
  switch (func) {
    case "sin":
      return Math.sin(x);
    case "cos":
      return Math.cos(x);
    case "parabola":
      return x * x;
    default:
      return 0;
  }
}
