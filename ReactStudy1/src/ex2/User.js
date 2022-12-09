import React from "react";


class User extends React.Component {
    constructor(props) {
      super(props);
      this.state = {value: '', sex:'남자'};
      

  
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({value: event.target.value});
    }
    handleChangeSex(event){
        this.setState({sex: event.target.value});
    }
  
    handleSubmit(event) {
      alert('A name was submitted: ' + this.state.value +'sex:'+this.state.sex);
      event.preventDefault();
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            이름:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          <br/>성별:
          <select sex={this.state.sex} onChange={this.handleChangeSex}>
           <option sex="남자">남자</option>
           <option sex="여자">여자</option> 
          </select>
          </label>
          <input type="submit" value="Submit" />
        </form>
      );
    }
  }
  export default User;
//   function User(props){
//     const[name, setName]=useState("");
//     const[gender, setGender]=useState("남자");

//     const handleChangeName=(event)=>{
//         setName(event.target.value);
//     };
//     const handleChangeGender=(event)=>{
//         setGender(event.target.value);
//     };
//     const


//     return(
//         <form onSubmit={hanleSubmit}>
//             <br />
//             <label style={{padding:16}}>
//                 이름:
//                 <input type="text" value={}onChange={handleChangeName}/>
//             </label>
//             <br /><br />
//             <label

//         </form>
//     )
//   }