import HeaderCSS from "./Header.module.css";
import Logo from "../Logo/Logo";
import SearchBar from "../SearchBar/SearchBar";

const Header = ({
  displayLikedBooks,
  setSearch,
}: {
  displayLikedBooks: any;
  setSearch: any;
}) => {
  return (
    <div id={HeaderCSS.flex}>
      <Logo />
      <SearchBar displayLikedBooks={displayLikedBooks} setSearch={setSearch} />
    </div>
  );
};

export default Header;
