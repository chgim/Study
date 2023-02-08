import React, {useState, useEffect} from "react";
import useCounter from "./useCounter";

const Max_CAPACITY=10;
const Min_CAPACITY=0;

function Accommodate(props){
    const[isFull, setIsFull]=useState(false);
    const[isEmpty,setIsEmpty]=useState(false);
    const[count, increaseCount, decreaseCount]=useCounter(0);

    useEffect(()=>{
        console.log("==================");
        console.log("useEffect() is called");
        console.log(`isFull:${isFull}`);
        console.log(`isEmpty:${isEmpty}`);
    });
    useEffect(()=>{
        setIsFull(count>=Max_CAPACITY);
        setIsEmpty(count<=Min_CAPACITY);
        console.log(`Current Count values:${count}`);
    },[count]);

    return(
        <div style={{padding:16}}>
            <p>{`총 ${count}명 수용했습니다.`}</p>

            <button onClick={increaseCount} disabled={isFull}>
                입장
            </button>
            <button onClick={decreaseCount} disabled={isEmpty}>퇴장</button>

            {isFull&&
                <p style={{color:"red"}}>정원이 가득찼습니다.</p>}
            {isEmpty&&
                <p style={{color:"blue"}}>입장해주세요.</p>}
        </div>
    );
}
export default Accommodate;