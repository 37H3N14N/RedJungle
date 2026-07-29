import React from 'react'
import './BookingTablet.css'

function BookingTablet({booking_data}) {
  return (
    <div className='individual_div_booking'>

        <div className='first_div_booking'>
            {booking_data[0].map((dict_data) => {
                return(
                    <div className='name_and_data'>
                        <div className='column_name_booking'>{dict_data['column_name']}:</div>
                        <div className='column_data_booking'>{dict_data['column_data']}</div>
                    </div>
                )
            })}
            <button className='cancel_button'>Cancel & Refund</button>
        </div>

        <div className='second_div_booking'>
            {booking_data[1].map((dict_data) => {
                return(
                    <div className='name_and_data'>
                        <div className='column_name_booking'>{dict_data['column_name']}:</div>
                        <div className='column_data_booking'>{dict_data['column_data']}</div>
                    </div>
                )
            })}
        </div>

        <div className='third_div_booking'>
            {booking_data[2].map((dict_data) => {
                return(
                    <div className='name_and_data'>
                        <div className='column_name_booking'>{dict_data['column_name']}:</div>
                        <div className='column_data_booking'>{dict_data['column_data']}</div>
                    </div>
                )
            })}
        </div>

        <div className='fourth_div_booking'>
            {booking_data[3].map((dict_data) => {
                return(
                    <div className='name_and_data'>
                        <div className='column_name_booking'>{dict_data['column_name']}:</div>
                        <div className='column_data_booking'>{dict_data['column_data']}</div>
                    </div>
                )
            })}
        </div>

    </div>
  )
}

export default BookingTablet
