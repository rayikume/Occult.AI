import React from "react";
import Logo from "../../Components/Logo/Logo";
import AdminCSS from "./Admin.module.css";
import AdminBook from "../../Components/AdminBook/AdminBook";
import AdminUser from "../../Components/AdminUser/AdminUser";

const Admin = () => {
  return (
    <>
      <Logo />
      <div className={AdminCSS.title}>Admin Panel</div>
      <div className={AdminCSS.content}>
        <AdminBook />
        <AdminUser />
      </div>
    </>
  );
};

export default Admin;
