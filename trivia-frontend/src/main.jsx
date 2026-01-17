import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import App from "./App";
import Root from "./routes/Root";
import CategoriesPage from "./routes/CategoriesPage";
import QuizPage from "./routes/QuizPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { index: true, element: <Root /> },
      { path: "categories", element: <CategoriesPage /> },
      { path: "quiz/:categoryId", element: <QuizPage />}
    ],
  }
]);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);