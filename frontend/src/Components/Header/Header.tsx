import HeaderCSS from "./Header.module.css";
import Logo from "../Logo/Logo";
import SearchBar from "../SearchBar/SearchBar";

const Header = ({
  displayLikedBooks,
  setSearch,
  setFilter,
}: {
  displayLikedBooks: any;
  setSearch: any;
  setFilter: any;
}) => {
  return (
    <div id={HeaderCSS.flex}>
      <Logo />
      <SearchBar
        displayLikedBooks={displayLikedBooks}
        setSearch={setSearch}
        setFilter={setFilter}
      />
    </div>
  );
};

export default Header;
