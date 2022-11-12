
import './App.css';
import MyFooter from './MyFooter';
import './MyHeader';
import MyHeader from './MyHeader';


function App() {
   let name="반갑습니다 여러분";
   const number=5;
   const style={
    App:{backgroundColor:"gold"}
   };
  return (
    <div className="App" style={style.App}>
      <MyHeader/>
      <header className="App-header">
        <h2>안녕 리액트 {name}</h2>
        {number}는: {number %2===0?"짝수":"홀수"}
      </header>
      <MyFooter/>
    </div>
  );
}

export default App;
