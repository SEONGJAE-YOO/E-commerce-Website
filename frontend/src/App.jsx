import {useState} from 'react'
import { Routes, Route, BrowserRouter } from 'react-router-dom'; // Import the 'Routes', 'Route', and 'BrowserRouter' components.
// import Home from './views/shop/home'; // Importing the 'Home' component.
import Login from './views/auth/Login'; // Import the 'Login' component.
import Register from './views/auth/Register'; // Import the 'Register' component.
import Logout from './views/auth/Logout'; // Import the 'Logout' component.
import ForgotPassword from './views/auth/ForgotPassword'; // Import the 'ForgotPassword' component.
import CreatePassword from './views/auth/createPassword';
import StoreHeader from './views/base/StoreHeader';
import StoreFooter from './views/base/StoreFooter';
// import MainWrapper from './layouts/MainWrapper';

import Products from './views/store/Products';
import ProductDetail from './views/store/ProductDetail';
import Cart from './views/store/Cart';

function App() { // Define the main 'App' component.
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <StoreHeader />
          <Routes>
            {/* <Route path="/" element={<Home />} /> */}
            <Route path="/login" element={<Login />} />
            <Route path='/register' element={<Register />} />      
            <Route path='/logout' element={<Logout />} />
            <Route path="/forgot-password" element={<ForgotPassword />} />
            <Route path="/create-new-password" element={<CreatePassword />} />
            <Route path="/" element={<Products />} />
            <Route path="/detail/:slug" element={<ProductDetail />} />
            <Route path="/cart" element={<Cart/>} />
          </Routes>
      <StoreFooter />
    </BrowserRouter> 
  )
}

export default App; // Export the 'App' component as the default export of this module.
