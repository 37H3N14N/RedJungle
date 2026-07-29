import React from 'react'
import './ServiceTablet.css'
import service_pic from '../images/shot_1.png' 

function ServiceTablet({service_tabular_data}) {
  return (

    <div className='main_div_service_tablet'>

        <div className='first_div_service'>
            {service_tabular_data[0].map((entity_name) => {
                return(
                    <div className='service_name'>{entity_name['service_name']}</div>
                )
            })}
        </div>

        <div className='second_div_service'>
            {service_tabular_data[1].map((entity_image_src) => {
                return(
                    <img src={service_pic} alt='service_pic'/>
                )
            })}
        </div>

        <div className='third_div_service'>
            {service_tabular_data[2].map((service_day_time_pair) => {
                return(
                    <div className='day_time_service_div'>
                        <div className='service_day_available'>{service_day_time_pair['service_day']}</div>
                        <div className='service_time_availble'>{service_day_time_pair['service_time']}</div>
                    </div>
                )
            })}
        </div>

        <div className='fourth_div_service'>
            <div className='service_ticket_name'>Tickets</div>
            <div className='service_ticket_state'>Available</div>
        </div>
        <div className='fifth_div_price'>
            <div className='service_price_name'>Price:</div>
            {service_tabular_data[3].map((service_price) => {
                return(
                    <div className='service_price_amount'>${service_price['service_price']}</div>
                )
            })}
        </div>
        <div className='sixth_div_service'>
            <button className='service_button'>More Info</button>
            <button className='book_service_button'>Book</button>
        </div>

    </div>
  )
}

export default ServiceTablet
