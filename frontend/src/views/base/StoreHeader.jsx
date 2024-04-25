import React, { useContext, useState, useEffect } from 'react'
import { useAuthStore } from '../../store/auth';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';


function StoreHeader() {
    const [search, setSearch] = useState("")

    const [isLoggedIn, user] = useAuthStore((state) => [
        state.isLoggedIn,
        state.user,
    ]);

    console.log("user().vendor_id", user().vendor_id);

    const navigate = useNavigate()

    const handleSearchChange = (event) => {
        setSearch(event.target.value);
        console.log(search);
    }

    const handleSearchSubmit = () => {
        navigate(`/search?query=${search}`)
    }

    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container">
                    <Link className="navbar-brand" to="/">E-commerce</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">

                            {/* <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" >
                                    Pages
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <li><a className="dropdown-item" href="#">About Us</a></li>
                                    <li><a className="dropdown-item" href="#">Contact Us</a></li>
                                    <li><a className="dropdown-item" href="#">Blog </a></li>
                                    <li><a className="dropdown-item" href="#">Changelog</a></li>
                                    <li><a className="dropdown-item" href="#">Terms & Condition</a></li>
                                    <li><a className="dropdown-item" href="#">Cookie Policy</a></li>

                                </ul>
                            </li> */}

                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" >
                                    Account
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <li><Link to={'/customer/account/'} className="dropdown-item"><i className='fas fa-user'></i> Account</Link></li>
                                </ul>
                            </li>


                        </ul>
                        <div className="d-flex">
                            <input onChange={handleSearchChange} name='search' className="form-control me-2" type="text" placeholder="Search" aria-label="Search" />
                            <button onClick={handleSearchSubmit} className="btn btn-outline-success me-2" type="submit">Search</button>
                        </div>
                        {isLoggedIn()
                            ?
                            <>
                                <Link className="btn btn-primary me-2" to={'/customer/account/'}>Account</Link>
                                <Link className="btn btn-primary me-2" to="/logout">Logout</Link>
                            </>
                            :
                            <>
                                <Link className="btn btn-primary me-2" to="/login">Login</Link>
                                <Link className="btn btn-primary me-2" to="/register">Register</Link>

                            </>
                        }
                        
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default StoreHeader