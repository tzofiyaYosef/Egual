import React, { useState, useEffect } from 'react';
import './Home.css';
import './Title.css';
import { useNavigate } from 'react-router-dom'

function Home() {
    const navigate = useNavigate();
    const [details, setDetails] = useState({
        userName: "",
        password: "",
    });

    useEffect(() => {
        console.log("In isRegistered");
    }, []);

    const login = () => {
        const { userName, password } = details;
        console.log(`Username: ${userName}, Password: ${password}`);
        // axios.post('http://localhost:8000/api/login', { userName, password })
        // python - לשלוח לצד שרת 
    };

    return (
        <div id='home'>
            <div className="topnav">
                <button type="button" className="active" onClick={() => { navigate('/') }}>Home</button>
                <button type="button" onClick={() => { navigate('/about') }}>About</button>
                <button type="button" onClick={() => { navigate('/compare') }}>Compare photos</button>
                <div className="login-container">
                    <input type="text" placeholder="Username" id="userName" required onChange={(e) => { setDetails({ ...details, userName: e.target.value }) }} />
                    <input type="password" placeholder="Password" id="password" required onChange={(e) => { setDetails({ ...details, password: e.target.value }) }} />
                    <button type="button" onClick={() => { navigate('/signUp') }}>Sign up</button>
                    <button type="submit" onClick={login}>Login</button>
                </div>
            </div>
            <div className="focus_container">
                <div className="focus--mask">
                    <div className="focus--mask-inner">Egual</div>
                </div>
            </div>
        </div>
    );
}

export default Home;
