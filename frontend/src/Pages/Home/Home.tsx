import Header from "../../Components/Header/Header";
import BookShelf from "../../Components/BookShelf/BookShelf";
import Chatbox from "../../Components/Chatbox/Chatbox";
import HomeCSS from "./Home.module.css";

const Home = () => {
  return (
    <div className={HomeCSS.homepage}>
      <Header />
      <BookShelf />
      <Chatbox />
    </div>
  );
};

export default Home;
