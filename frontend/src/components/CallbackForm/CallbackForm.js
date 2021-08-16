import React, { useState } from "react";
import axios from "axios";
import DateTimePicker from "../DateTimePicker/DateTimePicker";

import "./CallbackForm.scss";
import FeedbackModal from "../FeedbackModal/FeedbackModal";

const CallbackForm = () => {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [company, setCompany] = useState("");
  const [email, setEmail] = useState("");
  const [subject, setSubject] = useState("");
  const [problemDescription, setProblemDescription] = useState("");
  const [datetime, setDatetime] = useState(null);

  const [visible, setVisible] = useState(false);
  const [modalText, setmodalText] = useState(["Success", "You send data!"]);

  const changeVisibility = () => {
    setVisible(!visible);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const submit_data = {
      name: name,
      phone_number: phone,
      company: company,
      email: email,
      subject: subject,
      problem_desciption: problemDescription,
      date_time_callback: datetime,
    };

    console.log("------>", submit_data);
    axios
      .post("http://127.0.0.1:8000/api/", submit_data)
      .then((res) => {
        setName("");
        setPhone("");
        setCompany("");
        setEmail("");
        setSubject("");
        setProblemDescription("");
        setDatetime(null);
        setmodalText(["Success", "You send data!"]);
        setVisible(true);
      })
      .catch((err) => {
        setmodalText(["Error", `${err}`]);
        console.log(err);
      });
  };

  return (
    <>
      <form className="callback-form" onSubmit={handleSubmit}>
        <h1>Callback Form</h1>
        <input
          className="input-class"
          type="text"
          name="name"
          value={name}
          onChange={(event) => setName(event.target.value)}
          placeholder={"Name:"}
          required
        />
        <input
          className="input-class"
          type="text"
          name="phone"
          value={phone}
          onChange={(event) => setPhone(event.target.value)}
          placeholder={"Phone:"}
        />
        <input
          className="input-class"
          type="text"
          name="company"
          value={company}
          onChange={(event) => setCompany(event.target.value)}
          placeholder={"Company:"}
        />
        <input
          className="input-class"
          type="email"
          name="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          placeholder={"Email:"}
          required
        />
        <input
          className="input-class"
          type="text"
          name="subject"
          value={subject}
          onChange={(event) => setSubject(event.target.value)}
          placeholder={"Subject:"}
          required
        />
        <textarea
          name="problemDescription"
          value={problemDescription}
          onChange={(event) => setProblemDescription(event.target.value)}
          placeholder={"Problem Description:"}
          required
        />
        <DateTimePicker
          className="date-time-picker"
          onChange={(value) => setDatetime(value)}
        />

        <input className="btn" type="submit" value="send" />
      </form>
      <FeedbackModal
          visible={(() => (visible ? "flex" : "none"))()}
          changeVisibility={() => changeVisibility()}
          modalText={modalText}
        />
    </>
  );
};

export default CallbackForm;
