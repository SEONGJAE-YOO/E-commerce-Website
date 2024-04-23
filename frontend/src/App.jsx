import {useState} from 'react'
import { Routes, Route, BrowserRouter } from 'react-router-dom'; // Import the 'Routes', 'Route', and 'BrowserRouter' components.
import Login from './views/auth/Login'; // Import the 'Login' component.
import Register from './views/auth/Register'; // Import the 'Register' component.
import Logout from './views/auth/Logout'; // Import the 'Logout' component.

function App() { // Define the main 'App' component.
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path='/register' element={<Register />} />      
        <Route path='/logout' element={<Logout />} />
      </Routes>
    </BrowserRouter> 
  )
}

export default App; // Export the 'App' component as the default export of this module.
