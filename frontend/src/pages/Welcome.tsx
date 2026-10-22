import "./Welcome.css";

function Welcome() {

   return (
    <div className="welcome">
      <h1>What to Watch</h1>
      <p>Discover your next favourite movie or series.</p>

      <div className="buttons">
        <button>Login</button>
        <button>Register</button>
        <button>Continue as Guest</button>
      </div>
    </div>
  );
}

export default Welcome;