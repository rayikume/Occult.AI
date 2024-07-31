import HeaderCSS from "./Header.module.css";

const Header = () => {
  return (
    <div id={HeaderCSS.flex}>
      <div className={HeaderCSS.title}>Occult.AI</div>
      <div className={HeaderCSS.search_container}>
        <input type="text" className={HeaderCSS.search_engine} />
      </div>
    </div>
  );
};

export default Header;
