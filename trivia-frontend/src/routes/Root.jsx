import { Link } from "react-router-dom";
import "../styles/index.css"

export default function Root() {
    return (
        <>
            <h1>Welcome to the Trivia App!</h1>
            <p>Test your knowledge with fun trivia questions.</p>
            <Link to="/categories">
                <button>Start Quiz</button>
            </Link>
        </>
    )
}