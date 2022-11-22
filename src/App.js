import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import Diary from './pages/Diary';
import New from './pages/New';
import Edit from './pages/Edit';
import MyButton from './components/MyButton';
// import RouteTest from './components/RouteTest'
function App() {
    // const env=process.env;
    // env.PUBLIC_URL=env.PUBLIC_URL||"";
  return (
   <BrowserRouter>
    <div className="App">
      <h2>app.js</h2>
    <MyButton text={'버튼'} onClick={()=>alert("버튼 클릭")}
    type={"positive"}
    />
     <MyButton text={'버튼'} onClick={()=>alert("버튼 클릭")}
    type={"negative"}
    />
     <MyButton text={'버튼'} onClick={()=>alert("버튼 클릭")}
    />
      
      {/* <img src={process.env.PUBLIC_URL+`/assets/emotion1.png`}/>
      <img src={process.env.PUBLIC_URL+`/assets/emotion2.png`}/>
      <img src={process.env.PUBLIC_URL+`/assets/emotion3.png`}/>
      <img src={process.env.PUBLIC_URL+`/assets/emotion4.png`}/>
      <img src={process.env.PUBLIC_URL+`/assets/emotion5.png`}/> */}
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/new" element={<New />}/>
        <Route path="/edit" element={<Edit />}/>
        <Route path="/diary/:id" element={<Diary />}/> {/*diary에는 아이디가 없는 일기가 없음.*/}
      </Routes>
      {/* <RouteTest /> */}
    </div>
    </BrowserRouter>
  );
}

export default App;
