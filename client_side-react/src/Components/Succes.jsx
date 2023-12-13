import React from 'react';
import './Succes.css'
import { useNavigate } from 'react-router-dom';

const Succes = () => {
  const navigate = useNavigate();

  return (
    <main className="text-container">
      {/* <svg className="text-stroke">
        <text className="text" textAnchor="middle" x="50%" y="50%">
        You have successfully registered
        </text>
      </svg> */}
      <h1 className='succes'>You have successfully registered!!</h1>
      <h2>Start to see how it works</h2>
      <button className="btn" type="button" onClick={() => { navigate('/compare') }}>
        Compare photos
      </button>
    </main>
  );
};

export default Succes;
