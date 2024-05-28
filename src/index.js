import React from 'react';
import ReactDOM from 'react-dom/client';
import './static/index.css';
import reportWebVitals from './Lib/reportWebVitals';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from './App';
import Home from './Pages/Home.tsx';
import Register from './Pages/Register.tsx';
import Login from './Pages/Login.tsx'
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/Home",
        element: <Home />,
      },
      {
        path: "/Register",
        element: <Register />,
      },
      {path:"/Login",
        element:<Login />
      }
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode style={{alignItems:"stretch"}}>
      <RouterProvider style={{alignItems:"stretch"}} router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();