import React from "react";

const MyName=(props)=>{
    const {name, children}=props;
    return(
        <div>
            안녕하세요, 재 이름은{name}입니다.<br/>
            children 값은 {children}
            입니다.
        </div>
    )
};
MyName.defaultProps={
    name:'기본이름'
};
export default MyName;