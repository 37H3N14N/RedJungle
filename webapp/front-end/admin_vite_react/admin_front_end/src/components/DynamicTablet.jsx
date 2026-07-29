import React from 'react'
import './DynamicTablet.css'

function DynamicTablet({incoming_data, origin_card_title}) {
  return (
    <div className='main_dynamic_tablet_div'>

        <div className='origin_card_title'>{origin_card_title}</div>

        <div className='generated_card_data'>
            {incoming_data.map((name_data_pair) => {
                return(
                    <div className='name_data_column_pair'>
                        <div className='column_name_universal'>{name_data_pair['column_name']}:</div>
                        <div className='column_data_universal'>{name_data_pair['column_data']}</div>
                    </div>
                )
            })}

        </div>
        <div className='crud_button_section'>
            <button className='modify_dynamic_object'>Modify</button>
            <button className='delete_dynamic_object'>Delete</button>
        </div>

    </div>
  )
}

export default DynamicTablet