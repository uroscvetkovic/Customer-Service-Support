import React, { useState } from 'react'
import axios from 'axios'
import DateTimePicker from '../DateTimePicker/DateTimePicker'

import './CallbackForm.scss'

const CallbackForm = () => {

    const [name, setName] = useState('')
    const [phone, setPhone] = useState('')
    const [company, setCompany] = useState('')
    const [email, setEmail] = useState('')
    const [subject, setSubject] = useState('')
    const [problemDescription, setProblemDescription] = useState('')
    const [datetime, setDatetime] = useState(null)


    const handleSubmit = event => {
        event.preventDefault();
        const submit_data = {
            'name': name,
            'phone_number': phone,
            'company': company,
            'email': email,
            'subject': subject,
            'problem_desciption': problemDescription,
            'date_time_callback': datetime
        }

        console.log('------>', submit_data)
        axios.post('http://127.0.0.1:8000/api/', submit_data)
            .then(res => {
                console.log(res)
                setName('')
                setPhone('')
                setCompany('')
                setEmail('')
                setSubject('')
                setProblemDescription('')
                setDatetime(null)
            }).catch(err => {
                console.log(err)
            })
    }

    const validation = () => {

    }

    return (
        <form className='callback-form' onSubmit={handleSubmit}>
            <h1>Callback Form</h1>
            <input type='text' name="name" value={name} onChange={event => setName(event.target.value)} placeholder={'Name:'} required />
            <input type='text' name="phone" value={phone} onChange={event => setPhone(event.target.value)} placeholder={'Phone:'} />
            <input type='text' name="company" value={company} onChange={event => setCompany(event.target.value)} placeholder={'Company:'} />
            <input type='email' name="email" value={email} onChange={event => setEmail(event.target.value)} placeholder={'Email:'} required />
            <input type='text' name="subject" value={subject} onChange={event => setSubject(event.target.value)} placeholder={'Subject:'} required />
            <textarea name="problemDescription" value={problemDescription} onChange={event => setProblemDescription(event.target.value)} placeholder={'Problem Description:'} required />
            <DateTimePicker onChange={value => setDatetime(value)}/>
            <input type='submit' />
        </form>
    )
}

export default CallbackForm
