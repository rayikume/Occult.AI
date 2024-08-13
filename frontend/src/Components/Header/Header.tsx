import HeaderCSS from "./Header.module.css";
import Logo from "../Logo/Logo";
import SearchBar from "../SearchBar/SearchBar";

const Header = ({ displayLikedBooks }: { displayLikedBooks: any }) => {
  return (
    <div id={HeaderCSS.flex}>
      <Logo />
      <SearchBar displayLikedBooks={displayLikedBooks} />
    </div>
  );
};

export default Header;
