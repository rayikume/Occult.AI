import BookShelfCSS from "./BookShelf.module.css";
import { useEffect, useState } from "react";
import axios from "axios";
import Heart from "../../Assets/Heart.svg";
import ImageEmpty from "../../Assets/ImageEmpty.svg";
import EmptyStar from "../../Assets/EmptyStar.svg";

interface Book {
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

  console.log(books);

  return (
    <div className={BookShelfCSS.book_shelf}>
      {error && <div>{error}</div>}
      {books.map((book) => (
        <div className={BookShelfCSS.book_card} key={book.book_id}>
          <div className={BookShelfCSS.book_header}>
            <div className={BookShelfCSS.info_container}>
              <h1>{book.title}</h1>
              <div className={BookShelfCSS.more_info_container}>
                <h2>{book.author}</h2>
                <h2>{book.published_year}</h2>
              </div>
            </div>
            <img
              className={BookShelfCSS.like_icon}
              src={Heart}
              alt="Like Icon"
            ></img>
          </div>
          <div className={BookShelfCSS.imgContainer}>
            <div className={BookShelfCSS.book_img}>
              {book.thumbnail ? (
                <img className={BookShelfCSS.imgBook} src={book.thumbnail} />
              ) : (
                <img className={BookShelfCSS.empty} src={ImageEmpty} />
              )}
            </div>
          </div>
          <div className={BookShelfCSS.cardfooter}>
            <div className={BookShelfCSS.genre}>Genre: {book.genre}</div>
            <div className={BookShelfCSS.ratingContainer}>
              <img src={EmptyStar} />
              <div className={BookShelfCSS.rating}>{book.average_rating}</div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default BookShelf;
