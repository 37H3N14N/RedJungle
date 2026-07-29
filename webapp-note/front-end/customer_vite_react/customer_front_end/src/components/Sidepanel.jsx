import React from 'react'
import './Sidepanel.css'


function Sidepanel({page_change}) {
  return (
    <div className='side_panel_div'>
        <button className='side_panel_button' onClick={() => {page_change('Hotel Services')}}>Hotel Services</button>
        <button className='side_panel_button' onClick={() => {page_change('Rooms')}}>Rooms</button>
        <button className='side_panel_button' onClick={() => {page_change('Review')}}>Review</button>
        <button className='side_panel_button' onClick={() => {page_change('Bookings')}}>Bookings</button>
        <button className='side_panel_button' onClick={() => {page_change('Billing')}}>Billing</button>
    </div>
  )
}

export default Sidepanel