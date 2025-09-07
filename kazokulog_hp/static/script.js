document.getElementById("logForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = {
        name: form.name.value,
        date: form.date.value,
        place: form.place.value,
        content: form.content.value
    };

    const res = await fetch("/submit-report", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(formData)
    });

    const msg = await res.text();
    document.getElementById("resultMessage").textContent = msg;

    // ✅ 入力内容をクリアする
    form.reset();
});
