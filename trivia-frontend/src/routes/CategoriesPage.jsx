import { useEffect, useState } from "react";
import { fetchCategories } from "../services/api.js";
import "../styles/CategoriesPage.css";

export default function CategoriesPage() {
    const [categories, setCategories] = useState([]);

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
        <h2>
            Choose a Category
        </h2>

        <div className="categories-grid">
            {categories.map(cat => {
                const randomColor =
                colors[Math.floor(Math.random() * colors.length)];

        return (
            <div
                key={cat.id}
                className="category-card"
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
