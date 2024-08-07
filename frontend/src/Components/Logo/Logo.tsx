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
      {isBannerVisible && (
        <div className={LogoCSS.bannerOUT}>
          <div className={LogoCSS.tile} onClick={handleLogin}>
            Login/SignUp
          </div>
        </div>
        // <div className={HeaderCSS.banner}>
        //   <div className={HeaderCSS.tile}>Profile</div>
        //   <div className={HeaderCSS.tile}>Admin Panel</div>
        //   <div className={`${HeaderCSS.tile} ${HeaderCSS.logout}`}>
        //     Sign Out
        //   </div>
        // </div>
      )}
    </div>
  );
};

export default Logo;
