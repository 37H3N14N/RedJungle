import React from 'react'
import './DynamicSidePanel.css'

function DynamicSidePanel({first_b,second_b,third_b,fourth_b,fifth_b}) {
  return (
    <div className='main_dynamic_sidepanel_div'>
        <button className='first_dynamic_sidepanel_button'>SEARCH</button>
        <button className='second_dynamic_sidepanel_button'>{second_b}</button>
        <button className='third_dynamic_sidepanel_button'>{third_b}</button>
        <button className='fourth_dynamic_sidepanel_button'>{fourth_b}</button>
        <button className='fifth_dynamic_sidepanel_button'>{fifth_b}</button>
    </div>
  )
}

export default DynamicSidePanel