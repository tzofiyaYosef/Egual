import React, { useState, useEffect } from 'react';
import "./ProphilUser.css";
import axios from 'axios';

const ProphilUser = () => {
    const [details, setDetails] = useState({
        userName: "",
        password: "",
        firstName: "",
        lastName: "",
        gmail: "",
        phone: "",
    });

    useEffect(() => {
        const formData = new FormData()
        formData.append("id", JSON.stringify(localStorage.getItem("gmail")))
        axios.post('http://localhost:5000/ReturningtUser', formData)
            .then(res => {
                console.log(res.data);
                const userData = res.data; // המידע שחוזר מהשרת
                setDetails({
                    userName: userData.userName,
                    password: userData.password,
                    firstName: userData.firstName,
                    lastName: userData.lastName,
                    gmail: userData.gmail,
                    phone: userData.phone
                });
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    function update() {
        const { userName, password, firstName, lastName, gmail, phone } = details;
        const userExist = { userName, password, firstName, lastName, gmail, phone };
        const formData = new FormData()
        formData.append("userExist", JSON.stringify(userExist))
        formData.append("id", JSON.stringify(localStorage.getItem("gmail")))
        axios.post('http://localhost:5000/updateUser', formData)
            .then(res => {
                localStorage.setItem("gmail", document.getElementById("3").value)
                alert("User details have been successfully updated")
            })
            .catch(error => {
                console.error(error);
            });
    }

    return (
        <div class="containerPlace">
            <input className='diff' type="text" id="0" placeholder="שם פרטי" required onChange={(e) => { setDetails({ ...details, firstName: e.target.value }) }} value={details.firstName} />
            <input className='diff' type="text" id="1" placeholder="שם משפחה" required onChange={(e) => { setDetails({ ...details, lastName: e.target.value }) }} value={details.lastName} />
            <input className='diff' type="text" id="4" placeholder="שם משתמש" required onChange={(e) => { setDetails({ ...details, userName: e.target.value }) }} value={details.userName} />
            <input className='diff' type="text" id="2" placeholder="פלאפון" required onChange={(e) => { setDetails({ ...details, phone: e.target.value }) }} value={details.phone} />
            <input className='diff' type="text" id="5" placeholder="סיסמה" required onChange={(e) => { setDetails({ ...details, password: e.target.value }) }} value={details.password} />
            <input className='diff' type="email" id="3" placeholder="מייל" required onChange={(e) => { setDetails({ ...details, gmail: e.target.value }) }} value={details.gmail} />
            <input className='diff' type="button" id="signUp" value="עדכון" onClick={update} />
        </div>
    )
};

export default ProphilUser;