import React ,{useState} from "react";


const Counter2=(props)=>{


    console.log(props);
    const[count1,setCount1]=useState(props.initialValue);

    const add1=()=>{
        setCount1(count1+1);
    };
    
    const sub1=()=>{
        setCount1(count1-1);
    };
    const square1=()=>{
        setCount1(count1*count1);
    };

  
    

    return(
        <div>
            <h2>{count1}</h2>
            <button onClick={add1}>+</ button>
            <button onClick={sub1}>-</button>
            <button onClick={square1}>**</button>

            
        </div>
    );
};
export default Counter2;