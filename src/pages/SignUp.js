 import React,{useState} from "react"

 function SignUp()
 {  
    const [isValid,setIsValid]=useState(0);
    const [formData,setFormData]=useState({
        user_id:0,
        username:'',
        password:'',
    }
    );
    const [mess,sertMess]=useState({
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

        request.open("POST","http://127.0.0.1:8000/raport/signup/"   );

        request.onload=function ()
    {
       console.log(request.responseText);
    }

    request.send(fData);

    };
    
    return(
      <>
        <form onSubmit={e=>{sendForm(e)}}>
        <label>
            Username:
            <input className="usr" name="username" type="text" onChange={e=>updateForm("username",e)}/>
        </label>
        <label>
            Password:
            <input className="password" name="password" type="password" onChange={e=>updateForm("password",e)}/>
        </label>
        <input type="submit" value="Sign Up"/>
        </form>
      </>
    );
 }
 export default SignUp;