import "./Header.css";

const Header = () => {
  return (
    <div id="flex">
      <div className="title">Occult.AI</div>
      <div className="search_container">
        <input type="text" className="search_engine" />
      </div>
    </div>
  );
};

export default Header;
