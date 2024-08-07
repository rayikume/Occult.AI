import HeaderCSS from "./Header.module.css";
import Logo from "../Logo/Logo";
import SearchBar from "../SearchBar/SearchBar";

const Header = () => {
  return (
    <div id={HeaderCSS.flex}>
      <Logo />
      <SearchBar />
    </div>
  );
};

export default Header;
