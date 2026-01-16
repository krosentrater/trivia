import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root from "./routes/Root.jsx";
import CategoriesPage from "./routes/CategoriesPage.jsx";

const router = createBrowserRouter([
  { path: "/", element: <Root /> },
  { path: "/categories", element: <CategoriesPage /> },
]);

export default function App() {
  return <RouterProvider router={router} />;
}