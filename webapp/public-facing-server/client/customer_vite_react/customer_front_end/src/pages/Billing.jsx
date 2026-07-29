import React from 'react'
import './Billing.css'
import BillingTablet from '../components/BillingTablet'

const billing_data = [
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ],
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ],
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ],
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ],
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ],
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ],
  [
    {
      'column_name':'User',
      'column_data': 'Arrow'
    },
    {
      'column_name':'Email',
      'column_data': 'John @filicity.company'
    },
    {
      'column_name':'Status',
      'column_data': 'Pending'
    },
    {
      'column_name':'Bank',
      'column_data': 'Industrial Bank'
    },
    {
      'column_name':'Card',
      'column_data': 'Visa'
    },
    {
      'column_name':'Amount',
      'column_data': '597.57'
    },
    {
      'column_name':'Last four digits',
      'column_data': '5438'
    },
    {
      'column_name':'Created at',
      'column_data': '31stMarch3095'
    }
  ]

]


function Billing() {
  return (
    <div className='main_billing_div'>
      {billing_data.map((singular_tablet) => {
        return(
          <BillingTablet
            singular_bill = {singular_tablet}
          />
        )
      })
      }

    </div>

  )
}

export default Billing