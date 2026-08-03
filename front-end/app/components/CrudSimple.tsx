import { useState } from "react";
import '../styling/CrudSimple.css'



export default function CrudSimple() {
  return (

    <div className="main_crud_container">

        <div className="crud_container_one">
            <input/>
            <button>CREATE</button>
        </div>

        <div className="crud_container_two">
            <select>
                <option>Folder2</option>
                <option>Group4</option>
                <option>Note9</option>
            </select>
            <button>UPDATE</button>
        </div>

        <div className="crud_container_three">
            <button>DELETE</button>
        </div>

    </div>

  )}






