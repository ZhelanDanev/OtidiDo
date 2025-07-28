function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const el = document.querySelector('search-box');
if (el) {
  el.addEventListener("input", function () {
    const query = this.value;
    if (query.length < 2) return;

    fetch("/ajax/search/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ query: query })
    })
    .then(res => res.json())
    .then(data => {
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";
        data.results.forEach(item => {
            const el = document.createElement("div");
            el.textContent = `${item.title} – ${item.description}`;
            resultsDiv.appendChild(el);
        });
    })
    .catch(err => {
        console.error("Грешка при заявката:", err);
    });
});
