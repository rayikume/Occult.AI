import "./BookShelf.css";
import { useEffect, useState } from "react";
import axios from "axios";

interface Book {
  thumbnail: string;
  title: string;
  description: string;
  book_id: number;
  genre: string;
}

const BookShelf = () => {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/books");
        setBooks(response.data);
        setLoading(false);
      } catch (error) {
        setError("Error fetching data");
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="book_shelf">
      {error && <div>{error}</div>}
      {books.map((book) => (
        <div className="book_container" key={book.book_id}>
          <div className="book_img">
            <img src={book.thumbnail} alt={book.title} />
          </div>
          <div className="book_title">{book.title}</div>
        </div>
      ))}
    </div>
  );
};

export default BookShelf;
