import { useParams } from "react-router-dom";
import { use, useEffect, useState } from "react";
import { fetchQuestions } from "../services/api";
import "../styles/QuestionsPage.css";

export default function Quiz() {
    const { categoryId } = useParams(); // Get category ID from URL parameters
    const [questions, setQuestions] = useState([]); // Store fetched questions
    const [currentIndex, setCurrentIndex] = useState(0); // Track current question index
    const [score, setScore] = useState(0); // Track user score
    const [userAnswer, setUserAnswer] = useState(""); // Tracks user answer
    const [hasSubmitted, setHasSubmitted] = useState(false); // Tracks if user has submitted an answer
    const [isCorrect, setIsCorrect] = useState(null); // Tracks if the answer is correct

useEffect(() => {
    async function load() {
        const q = await fetchQuestions(categoryId);
        setQuestions(q);
    }
    load();
}, [categoryId]);

if (questions.length === 0) {
    return <div>Loading questions...</div>;
}

const currentQuestion = questions[currentIndex];


function handleSubmit() {
    const correct = userAnswer.trim().toLowerCase() === currentQuestion.correct_answer.trim().toLowerCase(); // Checks if the answer is correct
    setIsCorrect(correct);
    setHasSubmitted(true);
    // Increments user score if correct
    if (correct) {
        setScore(score + 1);
    }
}

function handleNext() {
    setUserAnswer("");
    setHasSubmitted(false);
    setIsCorrect(null);
    setCurrentIndex(currentIndex + 1);
}

    return (
        <div>

            <h1>Quiz Time</h1>

            <p><strong>Question {currentIndex + 1} of {questions.length}</strong></p>
            <p>{currentQuestion.question}</p>
            
            {!hasSubmitted && (
                <>
                    <input
                        type="text"
                        value={userAnswer}
                        onChange={(e) => setUserAnswer(e.target.value)}
                        placeholder="Type answer here..." />
                    
                    <button onClick={handleSubmit}>Submit Answer</button>
                </>
            )}

            {hasSubmitted && (
                <div>
                    {isCorrect ? (
                        <p style={{ color: 'green' }}>Correct!</p>
                    ) : (
                        <p style={{ color: 'red' }}>Incorrect! The correct answer was: {currentQuestion.correct_answer}</p>
                    )}
                    {currentIndex + 1 < questions.length ? (
                        <button onClick={handleNext}>Next Question</button>
                    ) : (
                        <div>
                            <p>Your final score is {score} out of {questions.length}</p>
                            <button onClick={() => window.location.href = '/categories'}>Play Again</button>
                        </div>
                    )}
                </div>
            )}
            
        </div>
    );
}
