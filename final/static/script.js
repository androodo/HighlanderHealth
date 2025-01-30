function getFoodRecommendation() {
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;
    const dietPlan = document.getElementById('dietPlan').value;

    // Make an AJAX request to the Flask backend
    fetch(`/recommend?weight=${weight}&height=${height}&dietPlan=${dietPlan}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('foodRecommendation').innerText = data.recommendation;
        });
}
