import { useState } from "react";
import '../styling/SignUp.css'



export default function SignUp() {
  return (
    <div className="main_container_signup">
        
        <div className="signup_container">

            <div className="cred_main_container">

                <div className="username_container" >
                    <div>USERNAME</div>
                    <input placeholder="username"/>
                </div>
                <div className="passcode_container" >
                    <div>PASSCODE</div>
                    <input type="password" placeholder="passcode"/>
                </div>

            </div>

            <div className="login_or_signup">
                <button>LogIn</button>
                <button>DELETE USER</button>
                <button>SignUp</button>
            </div>

        </div>

    </div>
  )};






