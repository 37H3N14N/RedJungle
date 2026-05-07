import React from 'react'
import './BillingTablet.css'


function BillingTablet({singular_bill}) {
  return (
    <div className='individual_transaction'>
      {singular_bill.map(({column_name,column_data}) => {
        return(
          <div className='data_id_pair'>
            <div className='column_name_billing'>{column_name}:</div>
            <div className='column_data_billing'>{column_data}</div>
          </div>
      )})
    }

    </div>
  )
}

export default BillingTablet

