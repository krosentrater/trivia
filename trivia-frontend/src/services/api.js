const BASE_URL = 'http://127.0.0.1:5000/api';

// Fetches list of categories from the backend API
export async function fetchCategories() {
  const response = await fetch(`${BASE_URL}/categories`);
  const data = await response.json();
  return data.trivia_categories;
}

// Fetches questions for a specific category from the backend API
export async function fetchQuestions(categoryId) {
    const response = await fetch(`${BASE_URL}/questions?category=${categoryId}`);
    const data = await response.json();
    return data.results;
}

// Submits a new score to the backend API
export async function submitScore(payload) {
    const response = await fetch(`${BASE_URL}/score`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    });
    const data = await response.json();
    return data;
}