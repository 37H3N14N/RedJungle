import { useState } from "react";
import '../styling/AdminPanel.css'


export default function AdminPanel() {
  return (
    <div className="main_container_admin">

        <div className="control_panel_container">

            <div className="control_panel_one">
                <button>ADD</button>
                <button>UPGRADE</button>
                <button>DEMOTE</button>
                <button>REVOKE</button>
            </div>

            <div className="options_control_panel">

                <div className="options_choice_container">

                    <select className="select_option_container">
                        <option>Group</option>
                        <option>Group2</option>
                        <option>Group7</option>
                    </select>

                    <select className="select_option_container">
                        <option>Folder</option>
                        <option>Folder34</option>
                    </select>

                    <select className="select_option_container">
                        <option>Note4</option>
                        <option>Note98</option>
                    </select>

                </div>
                <div className="options_search_container">
                    <button>QUERY</button>
                </div>

            </div>

            <div className="control_panel_two">
                <button>Normal</button>
                <button>Admin</button>
            </div>

        </div>

        <div className="member_overview_container">

            <div className="member_first_container">

                <div className="public_member_container">
                    Public Members
                </div>
                <div className="group_member_container">
                    Group Members
                </div>
            </div>

            <div className="member_second_container">

                <div className="folder_member_container">
                    Folder Members
                </div>
                <div className="note_member_container">
                    Note Members
                </div>

            </div>

        </div>

    </div>
  )}





