import React,{useState} from "react"
import {useCookies} from "react-cookie"
import "./Login.css"

function LogInForm()
{
  const [user,setUser]=useState("");
  const [password,setPassword]=useState("");
  const [cookies, setCookie] = useCookies(['sessionID']);


  function updateUser(e)
  {
      setUser(e.target.value);
  }

  function updatePassword(e)
  {
      setPassword(e.target.value);
  }


 const HandleRequest= async (e) =>
  {
    e.preventDefault();
    const request=new XMLHttpRequest();

    const fdata=new FormData();

    fdata.append("password",password);
    fdata.append("username",user);
  
    
    request.open("POST","http://127.0.0.1:8000/raport/login/");
    request.onload= () =>
    { 
      const res=JSON.parse(request.response);
      if(res.status===200){
      setCookie(res.name,res.value);
      window.location.pathname="/";
      }
    };
    request.send(fdata);
    
  }


 return (
    <>
    <div className="sdata">
      <form onSubmit={e=>{HandleRequest(e)}}>
      <div className="ti"> Log In Here</div>
      <label>
          Username<br></br>
          <input className="usr" name="username" type="text" onChange={e=>updateUser(e)}/>
      </label>
      <label>
          Password<br></br>
          <input className="pass" name="password" type="password" onChange={e=>updatePassword(e)}/>
      </label>
      <input className="sub" type="submit" value="Log In"/>
      <a className="lk" href="/signup">Sign up</a>
      </form>
      </div>
    </>
  );
}

export default LogInForm;