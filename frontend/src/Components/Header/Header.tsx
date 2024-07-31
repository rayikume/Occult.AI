import HeaderCSS from "./Header.module.css";

const Header = () => {
  return (
    <div id={HeaderCSS.flex}>
      <div className={HeaderCSS.title}>
        <div className={HeaderCSS.logo}>Occult.AI</div>
        <div className={HeaderCSS.userLogo}>USERLOGO</div>
      </div>
      <div className={HeaderCSS.search_container}>
        <button className={HeaderCSS.search_icon}>SEARCHICON</button>
        <input
          type="text"
          className={HeaderCSS.search_engine}
          placeholder="Type book title/genre/name of author"
        />
        <button className={HeaderCSS.search_icon}>FILTER</button>
        <div className={HeaderCSS.gap}></div>
        <button className={HeaderCSS.like_filter}>LIKE</button>
      </div>
    </div>
  );
};

export default Header;
