import React from 'react'
import './CreateTenant.css'

function CreateTenant() {
  return (
    <div className='main_create_tenant_div'>

      <div className='main_create_tenant_header'>CREATE TENANT & SUPER ADMIN</div>

      <div className='create_tenant_input_detail'>
        <input className='tenant_name_input' placeholder='Tenant name'/>
        <input className='subscription_plan_input' placeholder='Subscription plan'/>
      </div>

      <div className='create_super_admin_input_detail'>

        <div className='first_sub_create_super_admin_input'>
          <input className='first_name_input' placeholder='firstname'/>
          <input className='last_name_input' placeholder='lastname'/>
        </div>

        <div className='email_input_div'>
          <input className='email_input' placeholder='email'/>
        </div>

        <div className='second_sub_create_super_admin_input'>
          <input className='password_input' placeholder='password' type='password'/>
          <input className='confirm_password_input' placeholder='confirm password' type='password'/>
        </div>

      </div>

      <div className='create_tenant_button_div'>
        <button className='create_tenant_submit'>Create Tenant & Super Admin</button>
      </div>

    </div>
  )
}

export default CreateTenant