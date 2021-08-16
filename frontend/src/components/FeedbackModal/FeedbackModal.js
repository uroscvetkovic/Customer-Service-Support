import React from "react";

import "./FeedbackModal.scss";

const FeedbackModal = ({
  visible = "none",
  modalText = ["Success", "You sen data!"],
  changeVisibility,
}) => {
  return (
    <div className="feedback-modal" style={{ display: visible }}>
      <h1>{modalText[0]}</h1>
      <p>{modalText[1]}</p>
      <button onClick={changeVisibility}>Ok</button>
    </div>
  );
};

export default FeedbackModal;
