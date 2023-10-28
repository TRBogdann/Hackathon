import logo from './logo.svg';
import './App.css';
import SignUp from './pages/SignUp';
import Home from './pages/Home';
import LogInForm from './pages/Login';
import Raport from './pages/Raport';

function App(){

let currentPage;
  switch(window.location.pathname)
  {
    case "/":
      currentPage=<Home/>;
      break;

    case "/signup":
      currentPage=<SignUp/>
      break;
    
   case "/login":
    currentPage=<LogInForm/>
      break;
    
      case "/raportare":
        currentPage=<Raport/>
          break;

    default:
      currentPage=<Home/>;
  }
  return (
    <>
    {currentPage}
    </>
  );
}

export default App;
