import React from 'react'
import './Services.css'
import ServiceTablet from '../components/ServiceTablet'

const complete_services_data = [
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
  [
    [
      {
        'service_name':'MOVIE THEATRE'
      },
    ],
    [
      {
        'service_image':'http://something.com/images_oodsdlkf.jpg'
      },
    ],
    [
      {
        'service_day':'Thursday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Tuesday',
        'service_time': '1400hrs - 1600hrs'
      },
      {
        'service_day':'Saturday',
        'service_time': '1400hrs - 1600hrs'
      },
    ],
    [
      {
        'service_price':54
      },
    ],
  ],
]

function Services() {
  return (
    <div className='main_div_services'>
      {complete_services_data.map((singular_service_data) => {
        return(
          <ServiceTablet
            service_tabular_data={singular_service_data} 
          />
        )
      })}
    </div>
  )
}

export default Services