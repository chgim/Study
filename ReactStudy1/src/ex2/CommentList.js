import React from "react";
import Comment from "./Comment";

function CommentList(props){
    return(
        <div>
            <Comment name={"홍길동"}
            comment={"안녕하세요 ,길동입니다."}/>
            <Comment name={"임꺽정"}
            comment={"안녕하세요?,반갑습니다."}/>
            <Comment name={"이순신"}
            comment={"아직 12척의 배가 남아 있습니다."}/>
            <Comment name={"안창호"}
            comment={"큰일이건 작은일이건 네가 하는일을 정성껏 하라."}/>
            <Comment name={"김구"}
            comment={"내 힘으로 할 수 없는 일에 도전하지 않으면 내 힘으로 갈 수 없는 곳에 이를 수 없다."}/>
            <Comment name={"김정희"}
            comment={"가슴 속에 일 만권의 책이 들어 있으면 그것이 흘러 넘쳐 글이 되고 그림이 된다."}/>
            <Comment name={"유관순"}
            comment={"나라에 바칠 목숨이 오직 하나 밖에 없는 것만이 이 소녀의 유일한 슬픔입니다."}/>
        </div>
    );
}
export default CommentList;