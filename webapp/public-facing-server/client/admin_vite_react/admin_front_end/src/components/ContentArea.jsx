import React from 'react'
import './ContentArea.css'
import Rooms from '../pages/Rooms';
import Hotel from '../pages/Hotel';
import Tenant from '../pages/Tenant'
import Billing from '../pages/Billing'
import Reviews from '../pages/Reviews'
import Services from '../pages/Services'
import Users from '../pages/Users'
import Guests from '../pages/Guests'
import Analytics from '../pages/Analytics'
import AuditLogs from '../pages/AuditLogs'
import CreateTenant from '../pages/CreateTenant'
import Login from '../pages/Login'
import DynamicSidePanel from './DynamicSidePanel';



function ContentArea(props) {
    if (props.page === 'Rooms'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Rooms/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel
                    second_b={'CREATE'} 
                    />
                </div>
            </div>
        )
    }
    if (props.page === 'Hotel'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Hotel/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel
                    second_b={'CREATE'} 
                    />
                </div>
            </div>
        )
    }
    if (props.page === 'Tenant'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Tenant/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel/>
                </div>
            </div>
        )
    }
    if (props.page === 'Billing'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Billing/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel/>
                </div>
            </div>
        )
    }
    if (props.page === 'Reviews'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Reviews/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel/>
                </div>
            </div>
        )
    }
    if (props.page === 'Services'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Services/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel
                    second_b={'CREATE'} 
                    />
                </div>
            </div>
        )
    }
    if (props.page === 'Users'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Users/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel/>
                </div>
            </div>
        )
    }
    if (props.page === 'Guests'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Guests/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel/>
                </div>
            </div>
        )
    }
    if (props.page === 'Analytics'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <Analytics/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel/>
                </div>
            </div>
        )
    }
    if (props.page === 'AuditLogs'){
        return (
            <div className='content_area_main_div'>
                <div className='main_content_display_area'>
                    <AuditLogs/>
                </div>
                <div className='main_content_sidepanel_options'>
                    <DynamicSidePanel
                    second_b='something'
                    fifth_b='hello'
                    />
                </div>
            </div>
        )
    }
    if (props.page === 'Login'){
        return (
            <div className='content_area_main_div'>
                <Login/>
            </div>
        )
    }
    if (props.page === 'CreateTenant'){
        return (
            <div className='content_area_main_div'>
                <CreateTenant/>
            </div>
        )
    }

    else{
        return(
            <div className='content_area_main_div'>
                <Login/>
            </div>
        )
    }
}

export default ContentArea