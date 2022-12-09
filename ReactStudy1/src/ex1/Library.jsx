import React from "react";
import Book from "./Book";
import './book.css';

function Library(props){

    return(
        <div>
            <h1>봄에 읽기 좋은 책</h1>
            <hr/>
            <div>
            <Book img="qwe.jpg" name="홍길동전" author="고양이" numOfPage={300} price={2000}/>
            <Book img="wer.jfif" name="난중일기" author="강아지" numOfPage={400} price={4000}/>
            <Book img="rt.jfif" name="백범일지" author="병아리" numOfPage={500} price={7000}/>
            <Book img="ty.jpg" name="안중근전" author="송아지" numOfPage={600} price={3000}/>
            </div>  
            
        </div>
        
    );

}
export default Library;