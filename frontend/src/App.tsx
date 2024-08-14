import Home from "./Pages/Home/Home";
import Login from "./Pages/Login/Login";
import "./App.css";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Admin from "./Pages/Admin/Admin";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </Router>
  );
}

export default App;
