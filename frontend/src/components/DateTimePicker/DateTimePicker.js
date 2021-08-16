import React, { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

const DateTimePicker = (props) => {
  const [startDate, setStartDate] = useState(null);

  const isWeekday = (date) => {
    const day = date.getDay();
    return day !== 6;
  };

  const filterPassedTime = (date) => {
    const selectedDate = new Date(date);
    const selectedTime =
      selectedDate.getHours() + selectedDate.getMinutes() / 60;
    if (date.getDay() === 0) return 8 <= selectedTime && 13 >= selectedTime;
    else return 8 <= selectedDate.getHours() && 20 >= selectedTime;
  };

  return (
    <DatePicker
      placeholderText="Click to select date and time "
      selected={startDate}
      onChange={(date) => {
        setStartDate(date);
        props.onChange(date);
      }}
      showTimeSelect
      timeFormat="HH:mm"
      timeIntervals={30}
      timeCaption="Time"
      dateFormat="MMMM d, yyyy h:mm"
      selectsStart
      startDate={startDate}
      filterDate={isWeekday}
      filterTime={filterPassedTime}
    />
  );
};

export default DateTimePicker;
