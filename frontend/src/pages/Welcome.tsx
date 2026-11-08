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
        <button onClick={test}>Test Backend</button>
      </div>
    </div>
  );

}

async function test() {
  const response = await fetch("http://127.0.0.1:8000/movies/");


  const data = await response.json();

  console.log(data);
}
    

export default Welcome;