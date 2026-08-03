import { useState } from 'react'
import '../styling/NoteViewPage.css'


export default function NoteViewPage() {
  return (
    <div className="main_note_container">

        <div className="content_navbar_container">

          <div className='content_input_area'>
            <input/>
          </div>

          <div className='content_universal_control'>
            <button>CREATE</button>
            <button>EDIT</button>
            <button>UPDATE</button>
            <button>DELETE</button>
          </div>

        </div>

        <div className="content_area_container">
          Content Area
        </div>

    </div>

  )};


