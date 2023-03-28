import './App.css';
import { BrowserRouter as Router, Route , Routes} from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'

import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import SingupPage from './pages/SingupPage'
import ProfilePage from './pages/ProfilePage'
import ExpertPage from './pages/ExpertPage'
import Header from './components/Header'

function App() {
  return (
    <div className="App">
      <Router>
        <AuthProvider>
          <Header/>
          <Routes>
            <Route element = <HomePage/> path="/" exact/>
            <Route element = <LoginPage/> path="/login"/>
            <Route element = <SingupPage/> path="/singup"/>
            <Route element = <ProfilePage/> path="/profile"/>
            <Route element = <ExpertPage/> path="/expert"/>
          </Routes>
        </AuthProvider>
      </Router>

    </div>
  );
}

export default App;
