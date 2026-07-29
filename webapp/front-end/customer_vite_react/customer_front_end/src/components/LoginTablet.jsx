import React from 'react'
import './LoginTablet.css'

function LoginTablet() {
  return (
    <div className='main_div_login_tablet'>

        <div className='platform_message'>
            <h1>Welcome , Login</h1>
        </div>

        <div className='input_section_area'>
            <input className='email_password_div_input' type='email' name='email' placeholder='Email'/>
            <input className='email_password_div_input' type='password' name='password' placeholder='Password'/>
        </div>

        <div className='submit_button_div'>
          <button className='submit_button'>Login</button>
        </div>

    </div>
  )
}

export default LoginTablet