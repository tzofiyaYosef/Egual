import React, { useState } from 'react';
import './ComparePhotos.css';

const ComparePhotos = () => {
  const [imageSrc, setImageSrc] = useState('');

  function raise(event, str, bit) {
    if (bit === 1) {
      const image = document.createElement('img');
      image.setAttribute('class', str);
      const form = document.getElementsByName('form')[0];
      form.appendChild(image);
    }

    const selectedFile = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (event) {
      setImageSrc(event.target.result);
    };

    reader.readAsDataURL(selectedFile);
  }

  return (
    <div className="compare-photos-container">
      {imageSrc ? (
        <img src={imageSrc} alt="" className="compare-photos-image" />
      ) : (
        <div className="compare-photos-placeholder">
          <span className="compare-photos-placeholder-text">
            עוד לא נבחרה תמונה
          </span>
        </div>
      )}
      <input
        type="file"
        className="myFile"
        name="filename"
        onChange={(event) => raise(event, 'speacheImg', 0)}
      />
    </div>
  );
};

export default ComparePhotos;
