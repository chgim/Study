import React ,{useState} from "react";

const Counter=()=>{

    const [count1, setCount1]=useState(1);
    const [count2, setCount2]=useState(1);
    const add1=()=>{
        setCount1(count1+1);
    };
    
    const sub1=()=>{
        setCount1(count1-1);
    };
    const square1=()=>{
        setCount1(count1*count1);
    };

    const add2=()=>{
        setCount2(count2+1);
    };
    
    const sub2=()=>{
        setCount2(count2-1);
    };
    const square2=()=>{
        setCount2(count2*count2);
    };
    

    return(
        <div>
            <h2>{count1}</h2>
            <button onClick={add1}>+</ button>
            <button onClick={sub1}>-</button>
            <button onClick={square1}>**</button>

            <h2>{count2}</h2>
            <button onClick={add2}>+</ button>
            <button onClick={sub2}>-</button>
            <button onClick={square2}>**</button>
        </div>
    );
};
export default Counter;