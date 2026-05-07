import React from 'react'
import './ReviewTablet.css'
import profile_pic from '../images/shot_1.png'

function ReviewTablet({review_data}) {
  return (
    <div className='main_div_review_tablet'>
        {review_data.map((complete_review_tablet) => {
            return (
                <div className='main_div_review_tablet_container'>
                    <div className='star_and_button'>
                        <div className='star_rating'>{complete_review_tablet['star_rating']}/5.0</div>
                        <button className='picture_button'>Pics</button>
                    </div>
                    <div className='review_message_container'>
                        <div className='review_message'>{complete_review_tablet['review_message']}</div>
                    </div>
                    <div className='detailed_data'>
                        <div className='profile_picture'>
                            <img src={profile_pic} alt='profile_pic'/>
                        </div>
                        <div className='user_and_date'>
                            <div className='user_name'>{complete_review_tablet['user_name']}</div>
                            <div className='date'>{complete_review_tablet['date']}</div>
                        </div>
                    </div>
                </div>
            )
        })}
        </div>
  )
}

export default ReviewTablet