import React from 'react'
import './SignUpTablet.css'

function SignUpTablet() {
  return (
    <div className='main_div_signup_tablet'>

        <div className='signup_platform_message'>
            <h1>Welcome , SignUp</h1>
        </div>

        <div className='action_message'>
            <p className='action_message_text'>Create an Account</p>
        </div>

        <div className='signup_input_section_area'>
            
            <div className='signup_names_div'>
              <input className='names_div_input' type='text' name='first_name' placeholder='First name'/>
              <input className='names_div_input' type='text' name='second_name' placeholder='Second name'/>
            </div>

            <input className='email_password_div_input' type='email' name='email' placeholder='Email'/>
            <input className='email_password_div_input' type='password' name='password' placeholder='Password'/>

        </div>

        <div className='submit_button_div'>
          <button className='submit_button'>SignUp</button>
        </div>

    </div>
  )
}

export default SignUpTablet