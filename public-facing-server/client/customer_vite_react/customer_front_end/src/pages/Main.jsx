import React from 'react';
import './Main.css'
import Header from '../components/Header';
import Sidepanel from '../components/Sidepanel';
import ContentArea from '../components/ContentArea';
import { useState } from 'react';


const MainComponent = () => {
    const [CurrentPage,setCurrentPage] = useState('home');

    const selected_page = (page_name) => {
        setCurrentPage(page_name)
        console.log(page_name)
    };

    return(
        <div className='main'>
            <Header page_change={selected_page}/> 
            <div className='main_body'>
                <Sidepanel page_change={selected_page}/>
                <ContentArea page={CurrentPage}/>
            </div>
        </div>
    );
};

export default MainComponent;





