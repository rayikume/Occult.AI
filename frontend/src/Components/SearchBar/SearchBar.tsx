import SearchBarCSS from "./SearchBar.module.css";
import SearchIcon from "../../Assets/Search.svg";
import FilterIcon from "../../Assets/FilterIcon.svg";
import LikeIcon from "../../Assets/LikeIcon.svg";

const SearchBar = ({ displayLikedBooks }: { displayLikedBooks: any }) => {
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
      />
      <img
        className={SearchBarCSS.search_icon}
        src={FilterIcon}
        alt="Filter Icon"
      />
      <div className={SearchBarCSS.gap}></div>
      <img
        className={SearchBarCSS.like_filter}
        src={LikeIcon}
        alt="Like Icon"
        onClick={() => displayLikedBooks((prev: any) => !prev)}
      />
    </div>
  );
};

export default SearchBar;
