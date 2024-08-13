import SearchBarCSS from "./SearchBar.module.css";
import SearchIcon from "../../Assets/Search.svg";
import FilterIcon from "../../Assets/FilterIcon.svg";
import LikeIcon from "../../Assets/LikeIcon.svg";
import Heart from "../../Assets/Heart.svg";
import { useState } from "react";

const SearchBar = ({
  displayLikedBooks,
  setSearch,
}: {
  displayLikedBooks: any;
  setSearch: any;
}) => {
  const [isLikeClicked, setisLikeClicked] = useState(false);
  const [inputValue, setInputValue] = useState("");

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value;
    setInputValue(value);
    setSearch(value);
  };

  const handleClick = () => {
    setisLikeClicked(!isLikeClicked);
    displayLikedBooks((prev: any) => !prev);
  };

  return (
    <div className={SearchBarCSS.search_container}>
      <img
        src={SearchIcon}
        alt="Search Icon"
        className={SearchBarCSS.search_icon}
      />
      <input
        type="text"
        className={SearchBarCSS.search_engine}
        placeholder="Type book title/genre/name of author"
        value={inputValue}
        onChange={handleSearchChange}
      />
      <img
        className={SearchBarCSS.search_icon}
        src={FilterIcon}
        alt="Filter Icon"
      />
      <div className={SearchBarCSS.gap}></div>
      <img
        className={SearchBarCSS.like_filter}
        src={isLikeClicked ? Heart : LikeIcon}
        alt="Like Icon"
        onClick={handleClick}
      />
    </div>
  );
};

export default SearchBar;
