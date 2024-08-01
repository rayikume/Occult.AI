import HeaderCSS from "./Header.module.css";
import SearchIcon from "../../Assets/Search.svg";
import Logo from "../../Assets/Logo.svg";
import FilterIcon from "../../Assets/FilterIcon.svg";
import LikeIcon from "../../Assets/LikeIcon.svg";
import ProfileIcon from "../../Assets/ProfileIcon.svg";

const Header = () => {
  return (
    <div id={HeaderCSS.flex}>
      <div className={HeaderCSS.title}>
        <div className={HeaderCSS.logo}>
          <img src={Logo} alt="Logo" />
        </div>
        <img
          className={HeaderCSS.profileicon}
          src={ProfileIcon}
          alt="Profile Icon"
        />
      </div>
      <div className={HeaderCSS.search_container}>
        <img
          src={SearchIcon}
          alt="Search Icon"
          className={HeaderCSS.search_icon}
        />
        <input
          type="text"
          className={HeaderCSS.search_engine}
          placeholder="Type book title/genre/name of author"
        />
        <img
          className={HeaderCSS.search_icon}
          src={FilterIcon}
          alt="Filter Icon"
        />
        <div className={HeaderCSS.gap}></div>
        <img className={HeaderCSS.like_filter} src={LikeIcon} alt="Like Icon" />
      </div>
    </div>
  );
};

export default Header;
