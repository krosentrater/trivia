const BASE_URL = 'https://127.0.0.1:5000';

// Fetches list of categories from the backend API
export async function fetchCategories() {
  const response = await fetch(`${BASE_URL}/categories`);
  const data = await response.json();
  return data.categories;
}

// Fetches questions for a specific category from the backend API
export async function fetchQuestions(categoryId) {
    const response = await fetch(`${BASE_URL}/categories/${categoryId}/questions`);
    const data = await response.json();
    return data.questions;
}

// Submits a new score to the backend API
export async function submitScore(payload) {
    const response = await fetch(`${BASE_URL}/scores`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    });
    const data = await response.json();
    return data;
}