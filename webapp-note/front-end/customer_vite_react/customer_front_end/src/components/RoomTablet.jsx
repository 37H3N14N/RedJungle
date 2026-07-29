import React from 'react'
import './RoomTablet.css'
import product_pic from '../images/shot_1.png'

function FloatingTablet({image_src,price_tag,room_name,description}) {
  return (
        <div className='singular_tablet'>
            <div className='first_div'>
                <img className='product_img' src={product_pic} alt='space_walk'/>
            </div>

            <div className='second_div'>
                <div className='tablet_info'>
                    <p className='room_name'>{room_name}</p>
                    <p className='tablet_description'>{description}</p>
                </div>
                <div className='pricing'>
                    <strong>Price:</strong>
                    <p className='price_tag'>${price_tag}</p>
                </div>
                <div className='tablet_buttons'>
                    <button className='button_instance'>More Info</button>
                    <button className='button_instance'>Book</button>
                    <button className='button_instance'>Check reviews</button>
                </div>
            </div>

        </div>
  )
}

export default FloatingTablet