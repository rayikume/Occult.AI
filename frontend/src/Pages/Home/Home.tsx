import Header from "../../Components/Header/Header";
import BookShelf from "../../Components/BookShelf/BookShelf";
import HomeCSS from "./Home.module.css";
import ChatIcon from "../../Assets/ChatIcon.svg";

const Home = () => {
  return (
    <div className={HomeCSS.homepage}>
      <Header />
      <BookShelf />
      <div className={HomeCSS.chatlogo_container}>
        <img src={ChatIcon} className={HomeCSS.chatbot} />
      </div>
    </div>
  );
};

export default Home;
