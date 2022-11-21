import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import Diary from './pages/Diary';
import New from './pages/New';
import Edit from './pages/Edit';
import RouteTest from './components/RouteTest'
function App() {
  return (
   <BrowserRouter>
    <div className="App">
      <h2>app.js</h2>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/new" element={<New />}/>
        <Route path="/edit" element={<Edit />}/>
        <Route path="/diary/:id" element={<Diary />}/> {/*diary에는 아이디가 없는 일기가 없음.*/}
      </Routes>
      <RouteTest />
    </div>
    </BrowserRouter>
  );
}

export default App;
