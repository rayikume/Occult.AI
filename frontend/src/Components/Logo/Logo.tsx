import { useState } from "react";
import LogoCSS from "./Logo.module.css";
import LogoBook from "../../Assets/LogoBook.svg";
import ProfileIcon from "../../Assets/ProfileIcon.svg";
import ProfileClicked from "../../Assets/ProfileClicked.svg";
import { useNavigate } from "react-router-dom";

const Logo = () => {
  const [isProfileClicked, setIsProfileClicked] = useState<boolean>(false);
  const [isBannerVisible, setIsBannerVisible] = useState<boolean>(false);
  const navigate = useNavigate();
  const token = localStorage.getItem("accessToken");

  const handleProfileClick = () => {
    handleProfile();
    toggleBannerVisibility();
  };

  const handleProfile = () => {
    setIsProfileClicked(!isProfileClicked);
  };

  const toggleBannerVisibility = () => {
    setIsBannerVisible(!isBannerVisible);
  };

  const handleLogin = () => {
    navigate("/login");
  };

  const handleSignOut = () => {
    localStorage.removeItem("accessToken");
    navigate("/login");
  };

  return (
    <div className={LogoCSS.title}>
      <div className={LogoCSS.logo}>
        <img src={LogoBook} alt="Logo" />
      </div>
      <div className={LogoCSS.profileContainer} onClick={handleProfileClick}>
        {isProfileClicked ? (
          <img src={ProfileClicked} />
        ) : (
          <img src={ProfileIcon} alt="Profile Icon" />
        )}
      </div>
      {isBannerVisible && token ? (
        <div className={LogoCSS.banner}>
          <div className={LogoCSS.tile}>Profile</div>
          <div className={LogoCSS.tile}>Admin Panel</div>
          <div
            className={`${LogoCSS.tile} ${LogoCSS.logout}`}
            onClick={handleSignOut}
          >
            Sign Out
          </div>
        </div>
      ) : isBannerVisible && !token ? (
        <div className={LogoCSS.bannerOUT}>
          <div className={LogoCSS.tile} onClick={handleLogin}>
            Login/SignUp
          </div>
        </div>
      ) : null}
    </div>
  );
};

export default Logo;
