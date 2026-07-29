import React from 'react'
import './Header.css'

function Header({page_change}) {
  return (
        <div className='main_header'>
                <div className='username'>Spiderman Meme</div>
                <div className='hotel_info'>
                    <div className='saas_name'>RedJungle</div>
                    <div className='dynamic_hotel_info'>
                        <button className='change_tenant_button'>BigBrain</button>
                        <button className='change_hotel_button'>MountainPeek</button>
                    </div>
                </div>
                <div className='profile'>
                    <button className='authorization_button' onClick={() => {page_change('Login')}}>Login</button>
                    <button className='authorization_button' onClick={() => {page_change('CreateTenant')}}>Create Tenant</button>
                </div>
        </div>
  )
}

export default Header