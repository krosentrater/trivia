import { useNavigate } from "react-router-dom";
import "../styles/index.css"
import { BASE_URL } from "../services/api";

export default function Root() {

    const navigate = useNavigate();

    async function handleStartQuiz() {
        const res = await fetch(`${BASE_URL}/token`);
        const data = await res.json();
        localStorage.setItem("token", data.token);
        navigate("/categories");
    }

    return (
        <>
            <h1>Welcome to the Trivia App!</h1>
            <p>Test your knowledge with fun trivia questions.</p>
            <button onClick={handleStartQuiz}>Start Quiz</button>
        </>
    )
}