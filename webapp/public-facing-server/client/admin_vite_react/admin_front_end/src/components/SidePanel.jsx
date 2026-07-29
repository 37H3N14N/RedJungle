import React from 'react'
import './SidePanel.css'


function SidePanel({page_change}) {
  return (
    <div className='side_panel_div'>
        <button className='side_panel_button' onClick={() => {page_change('Rooms')}}>Rooms</button>
        <button className='side_panel_button' onClick={() => {page_change('Hotel')}}>Hotel</button>
        <button className='side_panel_button' onClick={() => {page_change('Tenant')}}>Tenant</button>
        <button className='side_panel_button' onClick={() => {page_change('Billing')}}>Billing</button>
        <button className='side_panel_button' onClick={() => {page_change('Reviews')}}>Reviews</button>
        <button className='side_panel_button' onClick={() => {page_change('Services')}}>Services</button>
        <button className='side_panel_button' onClick={() => {page_change('Users')}}>Users</button>
        <button className='side_panel_button' onClick={() => {page_change('Guests')}}>Guests</button>
        <button className='side_panel_button' onClick={() => {page_change('Analytics')}}>Analytics</button>
        <button className='side_panel_button' onClick={() => {page_change('AuditLogs')}}>AuditLogs</button>
    </div>
  )
}

export default SidePanel