import { Routes, Route } from "react-router-dom";
import Welcome from "./pages/Welcome";
import Main from "./pages/Main";

function App() {
    return (
        <Routes>
            <Route path="/" element={<Welcome />} />
            <Route path="/main" element={<Main />} />
        </Routes>
    );
}

export default App;