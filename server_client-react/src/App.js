import Home from './Components/Home';
import './App.css';
import SignUp from './Components/SignUp';
import { Route, Routes } from 'react-router-dom';
import About from './Components/About';
import Compare from './Components/Compare';
import Footer from './Components/Footer';
import Start from './Components/Start';
// const {router, route} = require("react-router-dom");

function App() {
  return (
    <div className="App">
      <Home />
      <Routes>
        <Route path="/about" element={<About />} />
        <Route path="/signUp" element={<SignUp />} />
        <Route path="/compare" element={<Compare />} />
        <Route path="/" element={<Start />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
