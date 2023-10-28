import "./Home.css"
import mapLogo from "../media/map.png"
import serverLogo from "../media/serverdata.png"
import React,{useState} from "react";
import Cookies from "js-cookie";


function Home()
{

   
   return(
      <>
      <div className="wallpaper">
      <div className="images">
      <div>
      <a href="/raportare">< img className="i1" alt="img"  src={mapLogo}></img></a>
      <div className="t2">Raporteaza o problema</div>
      </div>
      <div>
      <a href="/"><img className="i1" alt="img" src={serverLogo}></img></a>
      <div className="t2">Date</div>
      </div>
      </div>
      </div>
      </>
    );
}

export default Home;