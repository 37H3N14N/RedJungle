import React from 'react'
import './Login.css'

function Login() {
  return (
    <div className='main_div_login'>

      <div className='login_div_message'>ADMIN LOGIN</div>

      <div className='tenant_and_hotel_div'>
          <div className='column_and_title_login'>
            <div className='login_column_name_title'>Tenant:</div>
            <div className='tenant_name_div'>Big Belly</div>
          </div>
          <div className='column_and_title_login'>
            <div className='login_column_name_title'>Hotel:</div>
            <div className='tenant_hotel_name_div'>Peek Zone</div>
          </div>
      </div>

      <div className='login_input_section_div'>
        <input className='username_login_input' placeholder='username'/>
        <input className='password_login_input' placeholder='password' type='password'/>
      </div>
      <div className='login_button_div'>
        <button className='login_submit_button'>Login</button>
      </div>

    </div>
  )
}

export default Login