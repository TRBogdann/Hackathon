import React from "react";
import {useState} from "react";
import "./Date.css"

function Data()
{

    const [data,setData]=useState("");

    const HandleRequest= async () =>
    {
      const request=new XMLHttpRequest();
      
      request.open("POST","http://127.0.0.1:8000/raport/data/");
      request.onload= () =>
      { 
        //const res=JSON.parse(request.response);    
       // setData(res.message);
      };
      request.send('send');
      
    }

    HandleRequest();
    return(
    <>
    <div className="col">{data} </div>
        
    </>
    );

}

export default Data;