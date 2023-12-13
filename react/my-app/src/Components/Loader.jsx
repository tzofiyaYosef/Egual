import React from 'react';
import './Loader.css';

const Loader = ({ loading }) => {
  return (
    <>
      {loading && (
        <div className="overlay">
          <div className="loader-container">
            <div className="loader"></div>
          </div>
        </div>
      )}
    </>
  );
};

export default Loader;