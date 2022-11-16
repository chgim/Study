import {useState} from 'react';

const EventPractice0 = () => {
    const [form, setForm] = useState({
        username : '',
        message : '',
        address:''
    })
    const {username, message, address} = form;
    const onChange = e => {
        const nextForm = {
            ...form,  
            [e.target.name] : e.target.value  
        }
        setForm(nextForm);
    }
    const onClick = () => {
        alert(username + ' : ' + message + ' : ' + address); 
        setForm({
            uername : '',
            message : '',
            address:''
        })
    }
    const onKeyPress = e => {
        if(e.key === 'Enter'){
            onClick();
        }
    }
    return (
        <div>
            <h1>이벤트 연습</h1>
            <input 
            type = 'text'
            name = 'username'
            placeholder = '홍길동'
            value = {username}
            onChange = {onChange}
            />
            <input
            type = 'text'
            name = 'message'
            placeholder = '-없이 번호만 입력하세요'
            value = {message}
            onChange = {onChange}
           
            />
            <input
            type = 'text'
            name = 'address'
            placeholder = '주소를 입력하세요'
            value = {address}
            onChange = {onChange}
            onKeyPress = {onKeyPress}
            />
            <button onClick = {onClick}>확인</button>
        </div>
    )
}

export default EventPractice0;