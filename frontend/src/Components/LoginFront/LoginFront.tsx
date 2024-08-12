import { useState } from "react";
import LoginFrontCSS from "./LoginFront.module.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";

interface User {
  username: string;
  password: string;
  role?: string;
}

const LoginFront = () => {
  const [username, setUsername] = useState("");
  const [usernameNEW, setUsernameNEW] = useState("");
  const [password, setPassword] = useState("");
  const [passwordNEW, setPasswordNEW] = useState("");
  const navigate = useNavigate();

  const handleSignUp = async (username: string, password: string) => {
    let role = "user";
    if (password === "admin") {
      role = "admin";
    }

    console.log(role);
    const newUser: User = {
      username: username,
      password: password,
      role: role,
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/users/register",
        {
          username: newUser.username,
          password: newUser.password,
          role: newUser.role,
        }
      );
      console.log(response);
      setUsernameNEW("");
      setPasswordNEW("");
      navigate("/");
    } catch (error) {
      console.error(error);
    }
  };

  const handleLogin = async (username: string, password: string) => {
    const existUser: User = {
      username: username,
      password: password,
    };

    try {
      const response = await axios.post("http://127.0.0.1:8000/users/login", {
        username: existUser.username,
        password: existUser.password,
      });
      console.log(response);
      setUsernameNEW("");
      setPasswordNEW("");
      if (response.status === 200) {
        localStorage.setItem("accessToken", response.data.access_token);
        setTokenExpiration(Date.now() + 10 * 60 * 1000);
      } else {
        console.error(response.data.detail);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const setTokenExpiration = (expirationTime: number) => {
    localStorage.setItem("tokenExpiration", expirationTime.toString());
  };

  return (
    <div className={LoginFrontCSS.front_container}>
      <div className={LoginFrontCSS.front}>
        <div className={LoginFrontCSS.headertext}>Log In</div>
        <div className={LoginFrontCSS.flexorg}>
          <label>Email</label>
          <input
            type="text"
            value={username}
            className={LoginFrontCSS.inputtext}
            placeholder="example@pwc.com"
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className={LoginFrontCSS.flexorg}>
          <label>Password</label>
          <input
            type="password"
            value={password}
            className={LoginFrontCSS.inputtext}
            placeholder="Placeholder/Input text"
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button
          className={LoginFrontCSS.highlightbutton}
          onClick={() => handleLogin(username, password)}
        >
          Log In
        </button>
        <div className={LoginFrontCSS.line}></div>
        <div className={LoginFrontCSS.headertext}>Sign Up</div>
        <div className={LoginFrontCSS.flexorg}>
          <label>Email</label>
          <input
            type="text"
            value={usernameNEW}
            className={LoginFrontCSS.inputtext}
            placeholder="example@pwc.com"
            onChange={(e) => setUsernameNEW(e.target.value)}
          />
        </div>
        <div className={LoginFrontCSS.flexorg}>
          <label>Password</label>
          <input
            type="password"
            value={passwordNEW}
            className={LoginFrontCSS.inputtext}
            placeholder="Placeholder/Input text"
            onChange={(e) => setPasswordNEW(e.target.value)}
          />
        </div>
        <button
          className={LoginFrontCSS.highlightbutton}
          onClick={() => handleSignUp(usernameNEW, passwordNEW)}
        >
          Sign Up
        </button>
      </div>
    </div>
  );
};

export default LoginFront;
