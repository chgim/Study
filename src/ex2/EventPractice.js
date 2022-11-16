import React from "react";
import { Component } from "react";

class EventPractice extends Component{
    state={
        message:'',
        username:'',
        address:''
    }
    handleChange=(e)=>{
        this.setState({
            [e.target.name]:e.target.value
        });
    }

    handleClick=()=>{
        alert(this.setState.username+':'+this.state.message);
        this.setState({
            username:'',
            message:'',
            address:''
        });
    }

    handleKeyPress=(e)=>{
        if(e.key==='Enter'){
            this.handleClick();
        }
    }

    render(){
        return(
            <div>
                <h1>이벤트 연습</h1>
                <input
                    type="text"
                    name="username"
                    placeholder="사용자명"
                    value={this.state.username}
                    onChange={this.handleChange}
            />
                <input
                    type="text"
                    name="message"
                    placeholder="아무거나 입력해보세요"
                    value={this.state.message}
                    onChange={this.handleChange}
            />
             <input
                    type="text"
                    name="address"
                    placeholder="주소를 입력하세요"
                    value={this.state.address}
                    onChange={this.handleChange}
                    onKeyPress={this.handleKeyPress}
            />
            <button onClick={this.handleClick}>확인</button>
            
                    </div>
        );
    }
}

export default EventPractice;