import './static/index.css';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from './Pages/Home';
import Register from './Pages/Register';
import Login from './Pages/Login'
import {createRoot} from "react-dom/client";
import PostPage from './Pages/PostPage';
import App from "./App";



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
      },
      {path:"/PostPage/:id",

        element:<PostPage/>
      }
    ],
  },
]);

const rootElement = document.getElementById('root');
// https://blog.logrocket.com/how-to-use-typescript-with-react-18-alpha/
if (!rootElement) throw new Error('Failed to find the root element');
const root =createRoot(rootElement);
root.render(<RouterProvider router={router}/>)

