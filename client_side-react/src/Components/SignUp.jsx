import { useState } from 'react';
import "./SignUp.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';

const SignUp = () => {
    const [details, setDetails] = useState({});
    const [showPassword1, setShowPassword1] = useState(false);
    const [showPassword2, setShowPassword2] = useState(false);

    const togglePasswordVisibility1 = () => {
        setShowPassword1(!showPassword1);
    };

    const togglePasswordVisibility2 = () => {
        setShowPassword2(!showPassword2);
    };

    return (
        <div className="containerPlace">
            <div className="row">
                <div className="col">
                    <input type="text" id="0" placeholder="first name" required />
                    <input type="text" id="1" placeholder="last name" required />
                    <input type="text" id="2" placeholder="phone" required />
                    <input type="email" id="3" placeholder="mail" required />
                    <input type="text" id="4" placeholder="user name" required />
                    <div className="password-container">
                        <div className="password-input">
                            <input type={showPassword1 ? "text" : "password"} id="5" placeholder="password" required />
                            <FontAwesomeIcon
                                icon={showPassword1 ? faEyeSlash : faEye}
                                className="eye-icon"
                                onClick={togglePasswordVisibility1}
                            />
                        </div>
                    </div>
                    <div className="password-container">
                        <div className="password-input">
                            <input type={showPassword2 ? "text" : "password"} id="6" placeholder="password authentication" required />
                            <FontAwesomeIcon
                                icon={showPassword2 ? faEyeSlash : faEye}
                                className="eye-icon"
                                onClick={togglePasswordVisibility2}
                            />
                        </div>
                    </div>
                    <input type="button" id="signUp" value="sign up" />
                    <br />
                </div>
                <div id="ex">
                    <div className="row">
                        <div className="col">
                            {/* <a href="index.html" style="background-color: #5c5c5c; color: white; border: none; padding: 10px 20px; text-decoration: none; display: inline-block; font-size: 16px; font-weight: bold;">Register</a> */}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SignUp;
