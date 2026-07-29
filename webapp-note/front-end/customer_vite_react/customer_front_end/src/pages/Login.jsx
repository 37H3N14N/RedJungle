import React from 'react'
import './Login.css'
import LoginTablet from '../components/LoginTablet'

function Login() {
  return (
    <div className='main_div_login'>
      <div className='login_tablet'>

        <div className='sub_login_tablet_one'>
          <div className='upper_sub_login_tablet_one'>
            <div className='hotel_name'>RedJungle</div>
            <button className='back_button'>Return</button>
          </div>

          <div className='lower_sub_login_tablet_one'>
            <div className='mission_phrase'>Something and Something</div>
            <div className='animation_div'>o-o-o-o</div>
          </div>
        </div>

        <div className='sub_login_tablet_two'>
          <LoginTablet/>
        </div>

      </div>
    </div>
  )
}

export default Login