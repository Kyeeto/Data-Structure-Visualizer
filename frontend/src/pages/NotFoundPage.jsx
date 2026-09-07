import { NavLink } from "react-router-dom";

function NotFoundPage(){
    return (
        <div>
            <h1>Page not found</h1>
            <p>That page does not exist</p>
            <NavLink to="/">Return home</NavLink>
        </div>
    )
}

export default NotFoundPage