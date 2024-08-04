import Header from "../../Components/Header/Header";
import BookShelf from "../../Components/BookShelf/BookShelf";
import HomeCSS from "./Home.module.css";

const Home = () => {
  return (
    <>
      <Header />
      <BookShelf />
      <div className={HomeCSS.footergap}></div>
    </>
  );
};

export default Home;
