import "./Welcome.css";
import { useNavigate } from "react-router-dom";
function Welcome() {
   const navigate = useNavigate();

   
   function handleClick() {
        navigate("/main");
    }

   return (
    <div className="welcome">
      <h1>What to Watch</h1>
      <p>Discover your next favourite movie or series.</p>

      <div className="buttons">
        <button>Login</button>
        <button>Register</button>
          <button onClick={handleClick}>
            Continue as Guest
        </button>
      </div>
    </div>
  );

}

    

export default Welcome;