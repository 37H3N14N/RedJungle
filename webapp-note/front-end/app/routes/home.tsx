import type { Route } from "./+types/home";
import '../styling/home.css'
import NoteViewPage from '../components/NoteViewPage'
import SignUp from '../components/SignUp'
import AdminPanel from '../components/AdminPanel'
import CrudSimple from '../components/CrudSimple'



export default function Home() {
  return (

   <div className="main_app_container">

    <div className="primary_container">
      <div className="dir_project_name">REDJUNGLE-[ WEBNOTE ]</div>

      <div className="current_workspace_initials">
        <div className="workspace_title">ADMIN</div>
        <div>-WORKSPACE</div>
      </div>

      <div className="database_overall_stats">

        <div>
          <div>GROUPS :</div>
          <div className="group_count_stat">40</div>
        </div>

        <div>
          <div>NOTES :</div>
          <div className="note_count_stat">129</div>
        </div>

        <div>
          <div>FOLDERS :</div>
          <div className="folder_count_stat">75</div>
        </div>

      </div>
    </div>

    <div className="secondary_container">

      <div className="left_main_container">

        <div className="group_container">
          <div className="group_container_window">GROUP</div>
          <CrudSimple/>
        </div>

        <div className="folder_container">
          <div className="folder_container_window">FOLDER</div>
          <CrudSimple/>
        </div>

      </div>

      <div className="center_main_container">
        <AdminPanel/>
      </div>

      <div className="right_main_container">

        <div className="notes_container">
          <div className="note_container_window">NOTES </div>
        </div>

        <div className="nav_buttons">  

          <div className="button_group">
            <button>ADMIN</button>
            <button>NOTE</button>
          </div>

          <div className="button_group">
            <button>PUBLIC</button>
            <button>PRIVATE</button>
          </div>

          <div className="button_group">
            <button>SIGN IN</button>
            <button>SIGN OUT</button>
          </div>

          <div className="button_group">
            <button>M.NOTES</button>
            <button>M.FOLDERS</button>
          </div>

          <div className="button_group">
            <button>M.GROUPS</button>
          </div>

        </div>
      </div>
    
    </div>
    
    
    </div> 


  );
}








