import { useEffect, useState } from "react";
import { fetchCategories } from "../services/api.js";
import { useNavigate } from "react-router-dom";
import "../styles/CategoriesPage.css";

export default function CategoriesPage() {
    const [categories, setCategories] = useState([]);

    const navigate = useNavigate();

    const colors = [
        "#FFB3BA",
        "#FFDFBA",
        "#FFFFBA",
        "#BAFFC9",
        "#BAE1FF",
        "#D7BAFF",
        "#FFC4E1",  
    ];

    useEffect(() => {
        fetchCategories().then(setCategories);
    }, []);

return (
    <div>
        <h1>
            Choose a Category
        </h1>

        <div className="categories-grid">
            {categories.map(cat => {
                const randomColor =
                colors[Math.floor(Math.random() * colors.length)];

        return (
            <div
                key={cat.id}
                className="category-card"
                onClick={() => navigate(`/quiz/${cat.id}`)}
                style={{ backgroundColor: randomColor }}
            >
                {cat.name}
            </div>
        );
        })}
        </div>
    </div>
    );
}
