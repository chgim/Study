import React from "react";
import {ReactDOM} from 'react-dom';

class Hello extends React.Component{
    render(){
        return <div>Hello{this.props.thWhat}</div>;
    }
}

export default Hello;