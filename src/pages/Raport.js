
import brokenLogo from "../media/broken.jpg"
import grabageLogo from "../media/garbage.webp"
import treeLogo from "../media/fallantree.jpg"
import React from "react";
import {useState} from "react";
import Cookies from "js-cookie";

function Raport()
{
    const [userData,setUserData]=useState(Cookies.get("session_id"));
    const [user,setUser]=useState("No User");

    let data=""
    if(userData){
     data=JSON.parse(userData);

    }
    const str1="http://127.0.0.1:8000/raport/locatie/?user_id="+data.user_id+"&description=pericol" ;
    const str2="http://127.0.0.1:8000/raport/locatie/?user_id="+data.user_id+"&description=gunoi" ;
    const str3="http://127.0.0.1:8000/raport/locatie/?user_id="+data.user_id+"&description=trotuar" ;

    return(
    <>
    {!userData ?    
    <>
     <div className="wallpaper">
        <div className="boxS">
        <h1>No User Found</h1>
        <a href="/login"><button>Log In</button></a>
        </div>
     </div>
    </>
    :
    <>
    <div className="wallpaper">
    <div className="images">
    <div>
    <a href={str1}>< img className="i1" alt="img"  src={treeLogo}></img></a>
    <div className="t2">Pericol</div>
    </div>
    <div>
    <a href={str2}><img className="i1" alt="img" src={grabageLogo}></img></a>
    <div className="t2">Gunoi</div>
    </div>
    <div>
    <a href={str3}><img className="i1" alt="img" src={brokenLogo}></img></a>
    <div className="t2">Trotuar</div>
    </div>
    </div>
    </div>

    </>
}
</>
    );
}

export default Raport