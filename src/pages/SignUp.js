 import React,{useState} from "react"
 import "./SignUp.css"

 function SignUp()
 {  
    const [isValid,setIsValid]=useState(0);
    const [formData,setFormData]=useState({
        user_id:0,
        username:'',
        password:'',
    }
    );
    const [mess,setMess]=useState({
        username:'',
        password:'',
    }
    );

    function updateForm(field,e)
    {
        let obj=formData;
        obj[field]=e.target.value;
        setFormData(obj);
    }


    function checkData()
    {

    }

    function sendForm(e)
    {
        e.preventDefault();
        checkData();
        console.log(formData);
        const fData= new FormData();
        for (const [key, value] of Object.entries(formData)) {
            fData.append(key,value);
        }

        const request=new XMLHttpRequest();

        request.open("POST","http://127.0.0.1:8000/raport/signup/");

        request.onload=function ()
    {
       console.log(request.responseText);
    }

    request.send(fData);

    };
    
    return(
      <>
      <div className="sdata">
        <form onSubmit={e=>{sendForm(e)}}>
        <div className="ti"> Sign Up Here</div>
        <label>
            Username<br></br>
            <input className="usr" name="username" type="text" onChange={e=>updateForm("username",e)}/>
        </label>
        <label>
            Password<br></br>
            <input className="pass" name="password" type="password" onChange={e=>updateForm("password",e)}/>
        </label>
        <input className="sub" type="submit" value="Sign Up"/>
        
        </form>
        </div>
      </>
    );
 }
 export default SignUp;