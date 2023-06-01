import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import './App.css';
import { useEffect } from 'react';
import axios from 'axios';
import PageTemplate from './pages';

function App() {
  useEffect(() => {
    const fetchData = async() => {
      await axios.get('http://localhost:8000/api/people/').then((res) => console.log(res.data))
    }
    fetchData();
  }, [])
  return (
    <div className="App">
      <PageTemplate/>
    </div>
  );
}

export default App;
