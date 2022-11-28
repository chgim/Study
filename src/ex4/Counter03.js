import React, {useEffect, useState} from "react";

function Counter03(props){
    
    const[count, setCount]=useState(0);

    useEffect(()=>{
        document.title=`you clicked ${count} times`;
    });

    const onIncrease = () => {
        setCount(count + 1);
      }
    
     


    return(
        <div>
            <p>총{count}번 클릭했습니다.</p>
          
            <button onClick={onIncrease}>+1</button>
           
        </div>
    );
};
export default Counter03;