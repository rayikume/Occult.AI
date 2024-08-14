import { useEffect, useState } from "react";
import AdminUserCSS from "./AdminUser.module.css";
import axios from "axios";

interface User {
  username: string;
  password: string;
  role: string;
}

const AdminUser = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem("accessToken");
        console.log(token);
        const response = await axios.get("http://127.0.0.1:8000/users/all", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        console.log(response);
        setUsers(response.data);
      } catch (error: any) {
        if (error.response.status === 401) {
          setError("Unauthorized access. Please log in.");
        } else {
          setError("Error fetching data");
          console.error("Error fetching data:", error);
        }
      }
    };

    fetchData();
  }, []);

  return (
    <div className={AdminUserCSS.userpanel}>
      <div className={AdminUserCSS.title}>Users</div>
      {error && <div>{error}</div>}
      <div className={AdminUserCSS.table_container}>
        {users.map((row) => (
          <div className={AdminUserCSS.rowU} key={row.username}>
            <div className={AdminUserCSS.username}>{row.username}</div>
            <div className={AdminUserCSS.role}>{row.role}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AdminUser;
