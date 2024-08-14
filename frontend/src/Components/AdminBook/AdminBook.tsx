import React, { useEffect, useState } from "react";
import AdminBookCSS from "./AdminBook.module.css";
import axios from "axios";

interface BookTable {
  book_id: number;
  title: string;
  thumbnail: string;
  published_year: string;
  author: string;
  subtitle: string;
  genre: string;
  description: string;
  average_rating: string;
}

const AdminBook = () => {
  const [books, setBooks] = useState<BookTable[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem("accessToken");
        console.log(token);
        const response = await axios.get("http://127.0.0.1:8000/books", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        console.log(response);
        setBooks(response.data);
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
    <div className={AdminBookCSS.bookpanel}>
      <div className={AdminBookCSS.title}>Books</div>
      {error && <div>{error}</div>}
      <div className={AdminBookCSS.table_container}>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th className={AdminBookCSS.theaderid}>Title</th>
              <th className={AdminBookCSS.theader}>Author</th>
              <th className={AdminBookCSS.theader}>Published Year</th>
              <th className={AdminBookCSS.theaderye}>Rating</th>
            </tr>
          </thead>
          <tbody>
            {books.map((row) => (
              <tr key={row.book_id}>
                <td className={AdminBookCSS.tdescid}>{row.title}</td>
                <td className={AdminBookCSS.tdesc}>{row.author}</td>
                <td className={AdminBookCSS.tdesc}>{row.published_year}</td>
                <td className={AdminBookCSS.tdescye}>{row.average_rating}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AdminBook;
