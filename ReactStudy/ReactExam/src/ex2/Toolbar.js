import React from "react";

const styles={
    Wrapper:{
        padding:16,
        display:"flex",
        flexDirection:"row",
        borderBottom:"1px solid grey",
    },
    greeting:{
        marginRight:8,
    },
};

function Toolbar(props){
    const{isLoggedIn,onClickLogin, onClickLogout}=props;
    return(
    <div style={styles.Wrapper}>
        {isLoggedIn&&<span style={styles.greeting}>
            즐거운 시간 되세요~!</span>}
        {!isLoggedIn&&<span style={styles.greeting}>
            어서오세요~!</span>}
            {isLoggedIn?(
                <button onClick={onClickLogout}>로그아웃
                </button>
            ):(
                <button onClick={onClickLogin}>로그인
                </button>
            )}
            
    </div>
    );
}
export default Toolbar;