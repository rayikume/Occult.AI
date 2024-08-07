import { useState } from "react";
import LoginFrontCSS from "./LoginFront.module.css";

const LoginFront = () => {
  const [username, setUsername] = useState("");
  const [usernameNEW, setUsernameNEW] = useState("");
  const [password, setPassword] = useState("");
  const [passwordNEW, setPasswordNEW] = useState("");

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
        <button className={LoginFrontCSS.highlightbutton}>Log In</button>
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
        <button className={LoginFrontCSS.highlightbutton}>Sign Up</button>
      </div>
    </div>
  );
};

export default LoginFront;
