import React from "react";

const students=[
   
    {
        
        name:"한영"
        },
        {
           
            name:"가온"
            },
            {
                
                name:"유리"
                },
                {
                    
                    name:"지원"
                    },
];

function AttenDanceBook(props){
    return(
        <ul>
            {students.map((student)=>{
                return<li>{student.name}</li>;
            })}
        </ul>
    );
}

export default AttenDanceBook;