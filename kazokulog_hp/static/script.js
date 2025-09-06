document.getElementById("reportForm").addEventListener("submit",async(e) => {
  e.preventDefault();
  const formData = {
    name: e.target.name.value,
    date:e.target.date.value,
    task: e.target.task.value,
    time: e.target.time.value
  };

  const res = await fetch("/submit-report",{
    method:"POST",
    headers: { "Content-Type": "application/json"},
    body: JSON.stringify(formData)
  });

  const msg = await res.text();
  document.getElementById("resultMessage").textContent = msg;
});