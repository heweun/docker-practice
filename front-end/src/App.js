import './App.css';
import React, { useState } from 'react';
import api from './api';

function App() {
  const [any, setAny] = useState([]); 
  const [formData, setFormData] = useState({
    content: ''
  });

  const fetchAny = async () => {
    const response = await api.get('/get');
    const data = Array.isArray(response.data) ? response.data : [response.data];
    setAny(data);
  };

  const handleInputChange = (event) => {
    const value = event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await api.post('/add', formData);
    setFormData({
      content: ''
    });
  };

  return (
    <>
      <div className='main'> 
        <div className='top'>
          <form onSubmit={handleSubmit}>
            <label htmlFor='content'>
            </label>
            <input type='text' name='content' placeholder="텍스트를 입력하세요" value={formData.content} onChange={handleInputChange} />
            <button type="submit">
              입력하기
            </button>
          </form>
        </div> 
        <div className='buttom'>
          <button onClick={fetchAny}>
            가져오기
          </button>
          {any.map((p, index) => (
            <div key={index} className='inner'>
              <h4>입력된 데이터는</h4> "{p.content}"
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default App;
