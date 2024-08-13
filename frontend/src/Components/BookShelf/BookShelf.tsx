import BookShelfCSS from "./BookShelf.module.css";
import { useEffect, useState } from "react";
import axios from "axios";
import Heart from "../../Assets/Heart.svg";
import ImageEmpty from "../../Assets/ImageEmpty.svg";
import EmptyStar from "../../Assets/EmptyStar.svg";
import HalfStar from "../../Assets/halfStar.svg";
import AlmostStar from "../../Assets/AlmostStar.svg";
import EmptyHeart from "../../Assets/EmptyHeart.svg";

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

const BookCard = ({
  book,
  onLikeToggle,
  isLiked,
}: {
  book: Book;
  onLikeToggle: (bookId: number) => void;
  isLiked: boolean;
}) => {
  const [flipped, setFlipped] = useState(false);

  const handleFlip = () => {
    setFlipped(!flipped);
  };

  return (
    <div className={BookShelfCSS.card}>
      <div
        className={`${BookShelfCSS.card_inner} ${
          flipped ? BookShelfCSS.flipped : ""
        }`}
      >
        <div className={`${BookShelfCSS.card_face} ${BookShelfCSS.front}`}>
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
              src={isLiked ? Heart : EmptyHeart}
              alt="Like Icon"
              onClick={() => onLikeToggle(book.book_id)}
            />
          </div>
          <div className={BookShelfCSS.imgContainer}>
            <div className={BookShelfCSS.book_img} onClick={handleFlip}>
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
              {+book.average_rating > 0 && +book.average_rating < 2 ? (
                <img src={EmptyStar} />
              ) : +book.average_rating >= 2 && +book.average_rating < 4 ? (
                <img className={BookShelfCSS.halfRating} src={HalfStar} />
              ) : (
                <img src={AlmostStar} />
              )}
              <div className={BookShelfCSS.rating}>{book.average_rating}</div>
            </div>
          </div>
        </div>
        <div className={`${BookShelfCSS.card_face} ${BookShelfCSS.back}`}>
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
              src={isLiked ? Heart : EmptyHeart}
              alt="Like Icon"
              onClick={() => onLikeToggle(book.book_id)}
            />
          </div>
          <div className={BookShelfCSS.desc} onClick={handleFlip}>
            {book.description}
          </div>
        </div>
      </div>
    </div>
  );
};

const BookShelf = ({
  onLikeToggle,
  likedBooks,
  showLikedBooks,
  search,
  filter,
}: {
  onLikeToggle: (id: number) => void;
  likedBooks: number[];
  showLikedBooks: boolean;
  search: string;
  filter: string;
}) => {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
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
        setLoading(false);
      } catch (error: any) {
        if (error.response.status === 401) {
          setError("Unauthorized access. Please log in.");
        } else {
          setError("Error fetching data");
          console.error("Error fetching data:", error);
        }
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const sortBooks = (books: Book[]) => {
    switch (filter) {
      case "mostRecent":
        return books.sort(
          (a, b) => parseInt(b.published_year) - parseInt(a.published_year)
        );
      case "earliest":
        return books.sort(
          (a, b) => parseInt(a.published_year) - parseInt(b.published_year)
        );
      case "topRated":
        return books.sort(
          (a, b) => parseFloat(b.average_rating) - parseFloat(a.average_rating)
        );
      case "leastRated":
        return books.sort(
          (a, b) => parseFloat(a.average_rating) - parseFloat(b.average_rating)
        );
      default:
        return books;
    }
  };

  const filteredBooks = sortBooks(
    books
      .filter((book) =>
        showLikedBooks ? likedBooks.includes(book.book_id) : true
      )
      .filter(
        (book) =>
          book.title.toLowerCase().includes(search.toLowerCase()) ||
          book.author.toLowerCase().includes(search.toLowerCase()) ||
          book.genre.toLowerCase().includes(search.toLowerCase())
      )
  );

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className={BookShelfCSS.book_shelf}>
      {error && <div>{error}</div>}
      {filteredBooks.map((book) => (
        <BookCard
          key={book.book_id}
          book={book}
          onLikeToggle={onLikeToggle}
          isLiked={likedBooks.includes(book.book_id)}
        />
      ))}
    </div>
  );
};

export default BookShelf;
