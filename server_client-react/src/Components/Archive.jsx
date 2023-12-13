import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Archive.css';
import Loader from './Loader';

const Archive = () => {
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState([]);
  const hasResults = result && result.length > 0;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const formData = new FormData();
        formData.append("id", localStorage.getItem('gmail'));
        const response = await axios.post('http://localhost:5000/viewingArchive', formData);
        setResult(response.data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const appendLeadingZeros = (num) => {
    return num < 10? `0${num}` : num;
  }

  return (
    <div className={`archive-container ${loading ? 'loading' : ''}`}>
      <Loader loading={loading} />
      {!loading && (
        <div>
          <div className='title'>Comparisons made</div>
          {hasResults ? (
            <div className='allCompare'>
              {result.sort((a, b) => new Date(b.comparisonDate) - new Date(a.comparisonDate)).map((item, i) => {
                const dt = new Date(item.comparisonDate);
                const formattedDate = `${appendLeadingZeros(dt.getDate())}/${appendLeadingZeros(dt.getMonth() + 1)}`;
                const formattedFullDate = `${appendLeadingZeros(dt.getDate())}/${appendLeadingZeros(dt.getMonth() + 1)}/${appendLeadingZeros(dt.getFullYear())}`;

                return (
                  <div className="card">
                    <div className="date">{formattedDate}</div>
                    <img className="imgEvevt" src={`data:image/jpeg;base64,${item.path1}`} alt="path1" />
                    <div className='titles'>
                      <h3>The results of the comparison</h3>
                      <h1 className='comparisonResult'>{item.comparisonResult}</h1>
                      <h3 className='different'>made on the date</h3>
                      <h3>{formattedFullDate}</h3>
                    </div>
                    <img className="imgEvevt" src={`data:image/jpeg;base64,${item.path2}`} alt="path2" />
                  </div>
                );
              })}
            </div>
          ) : (
            <div className='title'>No comparisons have been made yet</div>
          )}
        </div>
      )}
    </div>
  );
};

export default Archive;