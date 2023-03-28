import React, {useContext} from 'react'
import AuthContext from '../context/AuthContext'

const SingupPage = () => {
  let {singup} = useContext(AuthContext)
  return (
    <div>
      <form onSubmit={singup}>
        <label>Nom: </label><input type="text" name="first_name" placeholder="Nom" required/> <br/>
        <label>Prenom: </label><input type="text" name="last_name" placeholder="Prenom" required/><br/>
        <label>Email: </label><input type="text" name="email" placeholder="Email" required/><br/>
        <label>Date De Naissance: </label><input type="Date" name="DateDeNaissance" placeholder="Date De Naissance" required/><br/>
        <label>Enter Password: </label><input type="password" name="password" placeholder="Enter Password" required/><br/>
        <label>Confirm Password: </label><input type="password" name="Conf_password" placeholder="Enter Password mara okhra" required/><br/>
        <input type="submit"/>
      </form>
    </div>
  )
}
export default SingupPage
