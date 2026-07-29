import React from 'react'
import './BillingTablet.css'


function BillingTablet() {
  return (
    <div className='individual_transaction'>

      <div className='data_id_pair'>
        <div className='column_name'>User:</div>
        <div className='user_name'>Arrow</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>Email:</div>
        <div className='user_email'>john_diagle@filicity.company</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>Status:</div>
        <div className='status'>Pending</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>Bank:</div>
        <div className='bank_name'>Industrial Bank</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>Card:</div>
        <div className='card_brand'>Visa</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>Amount:</div>
        <div className='amount'>$857</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>last four digits:</div>
        <div className='card_last_four_digits'>7259</div>
      </div>

      <div className='data_id_pair'>
        <div className='column_name'>created at:</div>
        <div className='created_at'>31stMarch3095</div>
      </div>

    </div>
  )
}

export default BillingTablet

