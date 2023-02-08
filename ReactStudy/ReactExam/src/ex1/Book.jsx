import React from "react";
import './book.css';

function Book(props){

    return(
        
    <div className="container">
        
        <ul className="book-list">
        <li>
            <img src={`${props.img}`} alt="실패"/>
            <div className="caption">

            <h3>{`이 책의 이름은 ${props.name} 입니다.`}</h3>
            <p>{`저자:${props.author}`}</p>
            <p>{`총 ${props.numOfPage} 페이지로 이뤄져 있습니다.`}</p>
            <p>{`가격:${props.price}원`}</p>
            </div>
        </li>
        
        </ul>
    </div>
    )
}
export default Book;