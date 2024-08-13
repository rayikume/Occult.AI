import Header from "../../Components/Header/Header";
import BookShelf from "../../Components/BookShelf/BookShelf";
import Chatbox from "../../Components/Chatbox/Chatbox";
import HomeCSS from "./Home.module.css";
import { useState } from "react";

const Home = () => {
  const [likedBooks, setLikedBooks] = useState<number[]>([]);
  const [showLikedBooks, setShowLikedBooks] = useState(false);

  const handleLikeToggle = (bookId: number) => {
    setLikedBooks((prevLikedBooks) =>
      prevLikedBooks.includes(bookId)
        ? prevLikedBooks.filter((id) => id !== bookId)
        : [...prevLikedBooks, bookId]
    );
  };

  return (
    <div className={HomeCSS.homepage}>
      <Header displayLikedBooks={setShowLikedBooks} />
      <BookShelf
        onLikeToggle={handleLikeToggle}
        likedBooks={likedBooks}
        showLikedBooks={showLikedBooks}
      />
      <Chatbox />
    </div>
  );
};

export default Home;
